from crewai import Task
from tools import tool
from agents import thesis_researcher,thesis_writer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic} and possible thesis topics."
    "Focus on identifying most relevalent topics and the overall narrative."
    "Your final report should clearly articulate the key points, list of links for relevalent topics"
    "its research opportunities and scope"
  ),
  expected_output='A comprehensive list of top 5 thesis topics along with a long report on the latest AI research area.',
  tools=[tool],
  agent=thesis_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the research area."
    "This article should be easy to understand, compreshensive and future prospective in nature."
  ),
  expected_output='A 5 paragraph article on {topic} advancements and future research area formatted as markdown.',
  tools=[tool],
  agent=thesis_writer,
  async_execution=False,
  output_file='thesis-blog.md'  # Example of output customization
)