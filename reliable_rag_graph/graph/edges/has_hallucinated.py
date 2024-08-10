

from reliable_rag_graph.graph.definitions import GraphState


def has_hallucinated(state: GraphState) -> str:
    return "answer_grader"