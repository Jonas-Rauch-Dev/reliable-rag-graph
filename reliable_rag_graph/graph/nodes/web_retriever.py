

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("web_retriever")

def web_retriever(state: GraphState) -> GraphState:
    logger.debug(f"state: {state}")
    return state