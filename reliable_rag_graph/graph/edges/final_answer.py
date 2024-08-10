
from langgraph.graph import END

from reliable_rag_graph.graph.definitions import GraphState


def final_answer(state: GraphState) -> str:
    return END