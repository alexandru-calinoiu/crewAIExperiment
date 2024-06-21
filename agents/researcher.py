from crewai import Agent


def create_researcher_agent(search_tool, llm):
    researcher = Agent(
        role="Senior Researcher",
        goal="Uncover groundbreaking technologies in {topic}",
        verbose=True,
        backstory=(
            "Driven by curiosity, you're at the forefront of"
            "innovation, eager to explore and share knowledge that could change"
            "the world."
        ),
        llm=llm,
        tools=[search_tool],
        allow_delegation=True,
    )
    return researcher
