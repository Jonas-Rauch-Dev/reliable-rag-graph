

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("generater")

def generater(state: GraphState) -> GraphState:
    logger.debug(f"state: {state}")
    return state