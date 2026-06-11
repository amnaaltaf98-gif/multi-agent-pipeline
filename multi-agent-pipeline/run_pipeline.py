from my_agents.research_agent import research_agent
from my_agents.writer_agent import writer_agent
from my_agents.reviewer_agent import reviewer_agent


topic = "What is AI Engineering and how does it differ from traditional software engineering?"

print("Researching...")

research = research_agent(topic)

print("Writing...")

draft = writer_agent(research)

print("Reviewing...")

review = reviewer_agent(draft)

print("\nFINAL OUTPUT\n")
print(review)