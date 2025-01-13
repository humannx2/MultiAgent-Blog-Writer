from crewai import Agent
from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = LLM(model="groq/llama3-8b-8192", temperature=0.7, api_key=api_key)

planner=Agent(
    role="LinkedIn Content Planner",
    goal= "Plan engaging and facutally correct content on {topic} for LinkedIn Posts",
    backstory="You are working on planning an engaging and thought provoking post on {topic}"
    "You collect information that helps the audience to learn something new and educate them."
    "Your work is the basis for content writer to write an engaging post",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

writer=Agent(
    role="LinkedIn Content Writer",
    goal= "Write an accurate and factually true LinkedIn post on {topic}, providing an insightful opinion",
    backstory="You are working on writing a new opinion piece on {topic}"
    "Your writings are based on the work of LinkedIn Content Planner, who outlines the guidelines for writing the content"
    "You follow the main objectives and guidelines of the outline"
    "You also provide objective and impartial insight and back them up with references provided by the LinkedIn Content Planner",
    allow_delegation=False,
    verbose=True,
    llm=llm
)