from crewai import Agent, Crew, Task, Process, LLM
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
import sys
from pathlib import Path


@CrewBase
class YourCrewName:
    """Description of your crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Paths to your YAML configuration files
    # To see an example agent and task defined in YAML, checkout the following:
    # - Task: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    # - Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def agent_one(self) -> Agent:
        return Agent(
            config=self.agents_config["agent_one"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def task_one(self) -> Task:
        return Task(
            config=self.tasks_config["task_one"]  # type: ignore[index]
        )
