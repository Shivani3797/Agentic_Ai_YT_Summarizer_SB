from crewai import Task
from tools import yt_tool

from agents import blog_researcher,blog_writer

##Research Task
research_task=Task(
    description=(
        "Identify the video{topic}."
        "Get detailed imformation about the video from the channel."
    ), 
expected_output="A comprehensive 3 paragraphs long report based on the {topic} of video content.",
tools=[yt_tool],
agent=blog_researcher,
)

##writing task
write_task=Task(
    description=(
        "get the info from youtube channel on the topic {topic}."
    ),
    expected_output='Summarize the info from the youtube channel video on the topic{topic}',
    tools=[yt_tool],
    agent=blog_writer,
    asynce_execution=False,
    output_file="new-blog-post.md"  #Example of output customization
)