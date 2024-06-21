from crewai import Agent


def create_writer_agent(search_tool, llm):
    writer_agent = Agent(
        role="Writer",
        goal="Narrate compelling tech stories about {topic}",
        verbose=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft"
            "engaging narratives that captivate and educate, bringing new"
            "discoveries to light in an accessible manner."
        ),
        llm=llm,
        tools=[search_tool],
        allow_delegation=False,
    )
    return writer_agent
