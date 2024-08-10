

from reliable_rag_graph.graph.definitions import GraphState
from reliable_rag_graph.graph.logger import get_logger

logger = get_logger("has_hallucinated")

def has_hallucinated(state: GraphState) -> str:
    logger.debug(f"state: {state}")
    return "answer_grader"