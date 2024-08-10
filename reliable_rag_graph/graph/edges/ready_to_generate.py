

from reliable_rag_graph.graph.definitions import GraphState


def ready_to_generate(state: GraphState) -> str:
    return "generate"