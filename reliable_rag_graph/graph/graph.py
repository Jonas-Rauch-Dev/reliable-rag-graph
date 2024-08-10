from langchain_core.runnables import Runnable
from langgraph.graph import StateGraph

from reliable_rag_graph.graph.definitions import GraphState, InputType, OutputType
from reliable_rag_graph.graph.edges.rag_or_web import rag_or_web
from reliable_rag_graph.graph.edges.final_answer import final_answer
from reliable_rag_graph.graph.edges.has_hallucinated import has_hallucinated
from reliable_rag_graph.graph.edges.ready_to_generate import ready_to_generate
from reliable_rag_graph.graph.nodes.answer_grader import answer_grader
from reliable_rag_graph.graph.nodes.documents_grader import documents_grader
from reliable_rag_graph.graph.nodes.generater import generater
from reliable_rag_graph.graph.nodes.hallucinator import hallucinator
from reliable_rag_graph.graph.nodes.rag_retriever import rag_retriever
from reliable_rag_graph.graph.nodes.router import router
from reliable_rag_graph.graph.nodes.web_retriever import web_retriever


def create_graph() -> Runnable:
    workflow: StateGraph = StateGraph(GraphState)

    # Add graph nodes
    workflow.add_node("router", router)
    workflow.add_node("documents_grader", documents_grader)
    workflow.add_node("generater", generater)
    workflow.add_node("hallucinator", hallucinator)
    workflow.add_node("rag_retriever", rag_retriever)
    workflow.add_node("web_retriever", web_retriever)
    workflow.add_node("answer_grader", answer_grader)

    # TODO: add edges
    workflow.add_conditional_edges("router", rag_or_web)
    workflow.add_edge(["rag_retriever", "web_retriever"], "documents_grader")
    workflow.add_conditional_edges("documents_grader", ready_to_generate)
    workflow.add_edge("generater", "hallucinator")
    workflow.add_conditional_edges("hallucinator", has_hallucinated)
    workflow.add_conditional_edges("answer_grader", final_answer)

    workflow.set_entry_point("router")

    return workflow \
        .compile() \
        .with_types(input_type=InputType, output_type=OutputType)