from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import TavilySearchTool
from pydantic import BaseModel, Field


class GameConceptBrief(BaseModel):
    """ a conceptiual brief for a game """
    title: str = Field(description="Title of the game")
    subtitle: str = Field(description="Subtitle of the game")
    description: str = Field(description="Description of the game")
    features: list[str] = Field(description="Features of the game")
    art: list[str] = Field(description="Art of the game")
    music: list[str] = Field(description="Music of the game")
    sound: list[str] = Field(description="Sound of the game")
    reasoning: str = Field(description="Reasoning why this works as a browser game")

class GameDesign(BaseModel):
    """ a design for a game """
    title: str = Field(description="Title of the game")
    subtitle: str = Field(description="Subtitle of the game")
    description: str = Field(description="Description of the game")
    features: list[str] = Field(description="Features of the game")
    mechanics: list[str] = Field(description="Mechanics of the game")
    art: list[str] = Field(description="Art of the game")
    music: list[str] = Field(description="Music of the game")
    sound: list[str] = Field(description="Sound of the game")

@CrewBase
class Mabstructgamesstudio():
    """Mabstructgamesstudio crew"""

    agents: list[BaseAgent]
    tasks: list[Task]


    @agent
    def game_producer(self) -> Agent:
        return Agent(
            config=self.agents_config['game_producer'], # type: ignore[index]
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def game_creative_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['game_creative_strategist'], # type: ignore[index]
            verbose=True,
            tools=[TavilySearchTool()],
            allow_delegation=False,
        )


    @agent
    def game_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['game_designer'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
        )

    @task
    def game_production_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_production_task'], # type: ignore[index]
        )

    @task
    def game_ideation_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_ideation_task'], # type: ignore[index]
            # output_pydantic=GameConceptBrief,
        )

    @task
    def game_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_design_task'], # type: ignore[index],
            # output_pydantic=GameDesign,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Mabstructgamesstudio crew"""
        return Crew(
            agents=[self.game_creative_strategist(), self.game_designer()],
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.game_producer(),
            verbose=True,
            tracing=True,
        )
