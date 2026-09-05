def validation_agent(state):
    context = state.get("context", "")
    answer = state.get("answer", "")
    valid = bool(context.strip() and answer.strip())
    return {**state, "valid": valid}
