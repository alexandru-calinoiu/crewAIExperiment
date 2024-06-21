from crewai import Task


def create_write_task(search_tool, writer):
    write_task = Task(
        description=(
            "Compose an insightful article on {topic}."
            "Focus on the latest trends and how it's impacting the industry."
            "This article should be easy to understand, engaging, and positive."
        ),
        expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
        tools=[search_tool],
        agent=writer,
        async_execution=False,
        output_file="new-blog-post.md",  # Example of output customization
    )
    return write_task
