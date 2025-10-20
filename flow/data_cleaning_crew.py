from crewai import Agent, Crew, Task, Process, LLM
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
import sys
from pathlib import Path


@CrewBase
class DataEngineeringCrew:
    """Crew for data importing, cleaning, and transforming"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def data_integrity_anlayst(self) -> Agent:
        return Agent(
            config=self.agents_config["data integrity analyst"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def revenue_data_quality_validation(self) -> Task:
        return Task(
            config=self.tasks_config["revenue_data_quality_validation"]  # type: ignore[index]
        )


if __name__ == "__main__":
    crew = DataEngineeringCrew()
    print(dir(crew))
