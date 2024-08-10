

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("ready_to_generate")

def ready_to_generate(state: GraphState) -> str:
    logger.debug(f"state: {state}")
    return "generate"