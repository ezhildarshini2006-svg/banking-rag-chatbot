def supervisor_agent(state):
    question = state["question"].lower()
    banking_keywords = [
        "account", "loan", "interest", "credit card", "debit card",
        "transaction", "balance", "bank", "deposit", "withdraw",
        "emi", "transfer"
    ]
    route = "retrieval" if any(k in question for k in banking_keywords) else "retrieval"
    return {**state, "route": route}
