from dotenv import load_dotenv
from os import getenv
from fastapi import FastAPI, UploadFile, File, HTTPException, status
from typing import Annotated
from langserve import add_routes
from uvicorn import run
import filetype

from reliable_rag_graph.graph.graph import create_graph
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("server")

load_dotenv()

hostname: str = getenv("SERVER_HOSTNAME", "0.0.0.0")
port: int = int(getenv("SERVER_PORT", "8000"))

app = FastAPI(
    title="Reliable RAG Graph",
    version="0.1.0",
    description="A reliable RAG implementation using langgraph",
)


def check_file_type(file: UploadFile) -> bool:

    accepted_file_types = [
        "application/pdf",
        "pdf",
    ]

    file_info = filetype.guess(file.file)
    if file_info is None:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Could not determine file type",
        )

    detected_file_type = file_info.extension.lower()

    if(
        file.content_type not in accepted_file_types 
        or detected_file_type not in accepted_file_types
    ):
        logger.info(f"Invalid file type: {detected_file_type}")
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unsupported file type"
        )

    return detected_file_type


@app.post("/fileupload/")
async def upload_file(
    file: Annotated[UploadFile, File()]
):
    logger.info(f"file: {file}")
    file_type = check_file_type(file)

    # TODO: split file in chunks with corresponding file splitter



def start() -> None:
    runnable = create_graph()

    add_routes(
        app,
        runnable
    )

    run(app, host=hostname, port=port)

if __name__ == "__main__":
    start()