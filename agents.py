from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

#from langchain_community.llms import HuggingFaceHub

"""llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=os.getenv("huggingfacehub_api_token"),
    task="text-generation",
)
"""
# Creating a senior researcher agent for finding thesis with memory and verbose mode

thesis_researcher=Agent(
    role="Thesis topics Researcher",
    goal='Discover the latest topics in recent development in AI and GenAI research area and technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are at the driver seat for finding and looking for the new opportunities"
        "in finding research topics for thesis in Undergrad level in the area of Artificial Intelligence"

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing thesis topics 

thesis_writer = Agent(
  role='Writer',
  goal='Summarize the list of thesis topics along with brief discription on possible research approach and link of relevant topics {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
