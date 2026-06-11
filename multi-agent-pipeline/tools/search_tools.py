from agents import function_tool


@function_tool
def web_search(query: str) -> str:
    """Search the web."""

    return (
        f"Search results for: {query}\n"
        f"Note: This is a demo search tool."
    )


@function_tool
def save_research_notes(topic: str, notes: str) -> str:
    """Save notes."""

    return f"Research notes saved for {topic}"