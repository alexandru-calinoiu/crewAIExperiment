from crewai import Task


def create_research_task(search_tool, researcher):
    research_task = Task(
        description=(
            "Identify the next big trend in {topic}."
            "Focus on identifying pros and cons and the overall narrative."
            "Your final report should clearly articulate the key points,"
            "its market opportunities, and potential risks."
        ),
        expected_output="A comprehensive 3 paragraphs long report on the latest {topic}.",
        tools=[search_tool],
        agent=researcher,
    )
    return research_task
