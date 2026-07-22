from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import TavilySearchTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Mabstructgamesstudio():
    """Mabstructgamesstudio crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

   
    @agent
    def game_creative_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['game_creative_strategist'], # type: ignore[index]
            verbose=True,
            tools=[TavilySearchTool()]
        )


    @agent
    def game_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['game_designer'], # type: ignore[index]
            verbose=True,
        )

    @task
    def game_ideation_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_ideation_task'], # type: ignore[index]
        )

    @task
    def game_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_design_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Mabstructgamesstudio crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            tracing=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
