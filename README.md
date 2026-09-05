# Banking Multi-Agent RAG Assistant

AI-powered banking assistant built with Python, LangChain, LangGraph, LLMs, FAISS and Streamlit.

## Architecture
Supervisor Agent → Retrieval Agent → Banking Response Agent → Validation Agent → Final Answer

## Features
- Query routing with a Supervisor Agent
- Semantic document retrieval using FAISS and embeddings
- Banking-focused response generation with an LLM
- Basic response validation
- Streamlit user interface

## Setup
1. Create a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your OpenAI API key.
4. Run: `streamlit run app.py`

Do not commit `.env` or API keys to GitHub.
