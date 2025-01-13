from crewai import Crew, Process
from agents import writer,planner,editor
from tasks import plan,edit,write

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "How to learn genai"})
print(result)