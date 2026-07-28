from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, before_kickoff, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import TavilySearchTool
from pydantic import BaseModel, Field

from .tools.here_now_tool import deploy_to_here_now
from .tools.telegram_tool import send_telegram_message
from .tools.write_game_html_tool import set_game_title, verify_game_html, write_game_html


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

    @before_kickoff
    def bind_game_title(self, inputs: dict) -> dict:
        set_game_title(str(inputs.get("game_title", "")))
        return inputs

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

    @agent
    def game_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['game_developer'], # type: ignore[index]
            llm=LLM(model="anthropic/claude-opus-4-8", max_tokens=64000, timeout=900),
            verbose=True,
            allow_delegation=False,
            tools=[write_game_html, verify_game_html],
        )

    @agent
    def game_tester(self) -> Agent:
        return Agent(
            config=self.agents_config['game_tester'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def game_deployer(self) -> Agent:
        return Agent(
            config=self.agents_config['game_deployer'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            tools=[deploy_to_here_now, send_telegram_message],
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

    @task
    def game_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_development_task'], # type: ignore[index]
        )

    @task
    def game_testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_testing_task'], # type: ignore[index]
        )

    @task
    def game_deployment_task(self) -> Task:
        return Task(
            config=self.tasks_config['game_deployment_task'], # type: ignore[index]
        )
   
    @crew
    def crew(self) -> Crew:
        """Creates the Mabstructgamesstudio crew"""
        return Crew(
            agents=self.agents,
            tasks=[
                self.game_ideation_task(),
                self.game_design_task(),
                self.game_development_task(),
                self.game_testing_task(),
                self.game_deployment_task(),
                self.game_production_task(),
            ],
            process=Process.sequential,
            verbose=True,
            tracing=True,
        )
