
from os import getenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("upsert_file")

async def upsert_file(file_path: str, file_type: str):
    # TODO: check that the file is not already stored in the db (meta data filename query)

    logger.info(f"starting to split {file_path}")
    # Load the file page wise asynchronously
    async for document in PyPDFLoader(file_path).alazy_load():
        pass
        # TODO: Split the document into chunks
        # TODO: Calculate embeddings for the chunks
        # TODO: upload the embedded chunks into the database