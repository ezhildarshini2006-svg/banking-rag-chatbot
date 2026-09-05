from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from pathlib import Path
from langgraph.graph import StateGraph, END
from agents.supervisor import supervisor_agent
from agents.retrieval_agent import retrieval_agent
from agents.banking_agent import banking_agent
from agents.validation_agent import validation_agent
from rag.vector_store import create_vector_store

st.set_page_config(page_title="Banking Multi-Agent RAG Assistant", page_icon="🏦")

@st.cache_resource
def load_vector_store():
    return create_vector_store("data/banking_faq.txt")

vector_store = load_vector_store()

def retrieval_node(state):
    return retrieval_agent(state, vector_store)

def build_graph():
    workflow = StateGraph(dict)
    workflow.add_node("supervisor", supervisor_agent)
    workflow.add_node("retrieval", retrieval_node)
    workflow.add_node("banking", banking_agent)
    workflow.add_node("validation", validation_agent)
    workflow.set_entry_point("supervisor")
    workflow.add_edge("supervisor", "retrieval")
    workflow.add_edge("retrieval", "banking")
    workflow.add_edge("banking", "validation")
    workflow.add_edge("validation", END)
    return workflow.compile()

graph = build_graph()

st.title("🏦 Banking Multi-Agent RAG Assistant")
st.write("Ask questions about accounts, loans, cards, deposits and transactions.")

question = st.text_input("Enter your banking question:")

if st.button("Ask Assistant"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing your query..."):
            result = graph.invoke({"question": question})
        st.subheader("Answer")
        st.write(result.get("answer", "Unable to generate an answer."))
        with st.expander("Retrieved Context"):
            st.write(result.get("context", "No context retrieved."))
