
from typing import TypedDict
from langchain_core.pydantic_v1 import BaseModel


class InputType(BaseModel):
    pass


class OutputType(BaseModel):
    pass


class GraphState(TypedDict, total = False):
    pass
