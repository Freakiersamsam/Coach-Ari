from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class PersonalGrowthCoach():
    """PersonalGrowthCoach crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            description="Research the topic: {topic}",
            agent=self.researcher(),
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            description="Write a report on the research findings.",
            agent=self.reporting_analyst(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.reporting_analyst()],
            tasks=[self.research_task(), self.reporting_task()],
            process=Process.sequential,
        )
