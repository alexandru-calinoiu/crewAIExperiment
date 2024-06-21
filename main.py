import os
from dotenv import load_dotenv
from crewai import Crew, Process
from crewai_tools import SerperDevTool
from agents import create_researcher_agent, create_writer_agent
from tasks import create_research_task, create_write_task
from langchain_openai import AzureChatOpenAI


load_dotenv()

azure_llm = AzureChatOpenAI(
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)


def main():
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
    search_tool = SerperDevTool()

    researcher = create_researcher_agent(search_tool=search_tool, llm=azure_llm)
    writer = create_writer_agent(search_tool=search_tool, llm=azure_llm)

    research_task = create_research_task(search_tool=search_tool, researcher=researcher)
    write_task = create_write_task(search_tool=search_tool, writer=writer)

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        cache=True,
        max_rpm=100,
        share_crew=True,
        verbose=True,
        memory=True,
        embedder={
            "provider": "azure_openai",
            "config": {
                "model": os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT"),
                "deployment_name": os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT"),
            },
        },
    )

    result = crew.kickoff(inputs={"topic": "AI regression testing"})
    print(result)


if __name__ == "__main__":
    main()
