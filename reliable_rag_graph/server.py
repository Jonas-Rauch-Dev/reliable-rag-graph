from dotenv import load_dotenv
from os import getenv
from fastapi import FastAPI
from langserve import add_routes
from uvicorn import run
from langchain_openai import ChatOpenAI


def start() -> None:
    load_dotenv()

    hostname: str = getenv("SERVER_HOSTNAME")
    port: int = int(getenv("SERVER_PORT"))
    model: str = getenv("OPENAI_MODEL")

    app = FastAPI(
        title="Reliable RAG Graph",
        version="0.1.0",
        description="A reliable RAG implementation using langgraph",
    )

    add_routes(
        app,
        ChatOpenAI(model=model)
    )

    run(app, host=hostname, port=port)


if __name__ == "__main__":
    start()