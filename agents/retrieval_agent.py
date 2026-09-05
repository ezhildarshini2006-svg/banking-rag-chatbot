def retrieval_agent(state, vector_store):
    question = state["question"]
    documents = vector_store.similarity_search(question, k=4)
    context = "\n\n".join(doc.page_content for doc in documents)
    return {**state, "context": context}
