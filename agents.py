from crewai import Agent

from tools import yt_tool


##Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog researcher from youtube video',
    goal='Get the relevant video content for the topic {topic} from yooutube channel',
    name='Senior Blog Content Researcher',
    verbose=True,
    memory=True,
    backstory=(
    "Expert in understanding videos in Ai Data Science, Machine Learning and GEN AI and providing suggestions"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

###creating a senior blog writer agent with yt tool

blog_writer= Agent(
    role='Blog Writer',
    goal='Narrate a compelling tech stories about the video{topic} from yt channel',
    verbose=True,
    memory= True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives2 that captivate and educate,bringing new"
        "discoveries to light in an acccessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)