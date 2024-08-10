
from langgraph.graph import END

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("final_answer")


def final_answer(state: GraphState) -> str:
    logger.debug(f"state: {state}")
    return END