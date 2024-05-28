from crewai import Crew,Process
from task import research_task,write_task
from agents import thesis_researcher,thesis_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[thesis_researcher,thesis_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Theis topic in AI and GenAI'})
print(result)