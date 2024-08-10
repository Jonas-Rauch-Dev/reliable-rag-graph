

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("router")

def router(state: GraphState) -> GraphState:
    logger.info("node router")
    return {
        "output": "hello"
    }