
from typing import TypedDict
from langchain_core.pydantic_v1 import BaseModel, Field


class InputType(BaseModel):
    input: str = Field(description="The user query")


class OutputType(BaseModel):
    output: str


class GraphState(TypedDict, total = False):
    input: str
    output: str
