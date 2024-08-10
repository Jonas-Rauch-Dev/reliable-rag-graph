from dotenv import load_dotenv
from os import getenv
from fastapi import FastAPI
from langserve import add_routes
from uvicorn import run
from langchain_openai import ChatOpenAI


def start() -> None:
    load_dotenv()

    hostname: str = getenv("SERVER_HOSTNAME", "0.0.0.0")
    port: int = int(getenv("SERVER_PORT", "8000"))
    model: str = getenv("OPENAI_MODEL", "gpt-3.5-turbo")

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