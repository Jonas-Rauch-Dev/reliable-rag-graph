

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("rag_retriever")


def rag_retriever(state: GraphState) -> GraphState:
    logger.debug(f"state: {state}")
    return state