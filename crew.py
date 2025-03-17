from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task


#Forming tech-foused crew with some enhanced configuration
crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,           #Sequential task is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

#Start task execution process
result = crew.kickoff(inputs={'topic': 'Energy Data Science Journey'})

print(result)