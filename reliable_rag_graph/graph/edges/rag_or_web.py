

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("rag_or_web")

def rag_or_web(state: GraphState) -> str:
    logger.debug(f"state: {state}")
    return "rag_retriever"