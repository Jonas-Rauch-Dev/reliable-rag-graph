
from os import getenv
from typing import List, Sequence

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

from chromadb import HttpClient

from reliable_rag_graph.graph.logger import get_logger

from uuid import uuid4

logger = get_logger("upsert_file")

async def upsert_file(file_path: str, file_type: str, chunk_size: int = 150, chunk_overlap: int = 0):
    # TODO: check that the file is not already stored in the db (meta data filename query)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    embedder: OpenAIEmbeddings = OpenAIEmbeddings(
        model=getenv("EMBEDDING_MODEL"),
    )


    print(f"DB url: {getenv('DB_HOST')}:{int(getenv('DB_PORT'))}")

    chroma_client = HttpClient(
        host=getenv("DB_HOST"),
        port=int(getenv("DB_PORT"))
    )
    collection = chroma_client.get_or_create_collection(getenv("DB_COLLECTION"))

    logger.info(f"starting to split {file_path}")
    # Load the file page wise asynchronously
    async for document in PyPDFLoader(file_path).alazy_load():
        # Split the document into chunks
        chunks: Sequence[Document] = await splitter.atransform_documents([document])
        contents, metadata ,ids = [], [], []
        for chunk in chunks:
            contents.append(chunk.page_content)
            metadata.append(chunk.metadata)
            ids.append(str(uuid4()))

        print(f"\nchunks: {chunks}")
        # Calculate embeddings for the chunks
        embeddings: List[float] = await embedder.aembed_documents(
            [chunk.page_content for chunk in chunks]
        )
        print(f"\nembeddings: {embeddings}")

        # upload the embedded chunks into the database
        collection.upsert(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadata,
            documents=contents
        )