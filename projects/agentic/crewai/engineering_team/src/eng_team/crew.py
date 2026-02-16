
from crewai import Agent, Crew, Process, Task, TaskOutput
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
#from typing import List
from eng_team.modules import ModuleList

@CrewBase
class EngineeringTeam():
    """EngineeringTeam crew"""

    # agents_config = 'config/agents.yaml'
    # tasks_config = 'config/tasks.yaml'
    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['engineering_lead'],
            verbose=True,
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",  # Uses Docker for safety
            max_execution_time=500, 
            max_retry_limit=3 
        )
    
    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            verbose=True,
        )
    
    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",  # Uses Docker for safety
            max_execution_time=500, 
            max_retry_limit=3 
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'],
            output_pydantic = ModuleList,
            callback = self.design_callback
        )

    def design_callback(self, output:TaskOutput) -> None:
        print('Design task completed, building tasks started..')
        m_list: ModuleList = output.pydantic
        print(m_list)
        agents = self.agents[1:] #except lead
        tasks = self.get_dynamic_tasks(m_list)
        sub_crew = Crew(
            tasks=tasks,
            agents=agents,
            process=Process.sequential,
            verbose=True
        )
        result = sub_crew.kickoff()
        print(result)

    def get_dynamic_tasks(self, m_list):        
        tasks = []
        classes = []
        module_list = []
        config_task = self.code_task()
        test_task = self.test_task()
        for i, module in enumerate(m_list.modules):
            classes.append(module.class_name)
            module_list.append(module.module_name)            
            tasks.append(
                Task(
                    name = f"{config_task.name}_{i}",  #unique naming
                    description = config_task.description.format(**vars(module)),
                    output_file = config_task.output_file.format(module_name = module.module_name),
                    expected_output = config_task.expected_output,
                    agent = self.backend_engineer()
                )
            )

            tasks.append(
                Task(
                    name = f"{test_task.name}_{i}",
                    description = test_task.description.format(**vars(module)),
                    output_file = test_task.output_file.format(module_name = module.module_name),
                    expected_output = test_task.expected_output,
                    agent = self.test_engineer()
                )
            )           
        
        f_task = self.frontend_task()
        f_task.description = f_task.description.format(class_list=classes, module_list=module_list)
        f_task.context = tasks.copy()
        tasks.append(f_task)
        return tasks

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'],
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task'],
        )

    @task
    def test_task(self) -> Task:
        return Task(
            config=self.tasks_config['test_task'],
        )   

    @crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=[self.engineering_lead()],
            tasks=[self.design_task()],
            process=Process.sequential,
            verbose=True,
        )