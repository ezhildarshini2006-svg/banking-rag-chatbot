from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are a banking assistant.

Answer the user's question using ONLY the provided context.
If the answer is not available in the context, say:
"The information is not available in the provided banking documents."

Context:
{context}

User Question:
{question}

Provide a clear and concise answer.
""")

def banking_agent(state):
    response = llm.invoke(
        prompt.format_messages(
            context=state.get("context", ""),
            question=state["question"]
        )
    )

    return {
        **state,
        "answer": response.content
    }