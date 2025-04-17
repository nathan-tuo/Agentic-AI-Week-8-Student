import os
from dotenv import load_dotenv
from crewai import Crew, Process
from gmail_agent import gmail_reader_agent
from gmail_service import fetch_mail
from tasks import gmail_todo

# Load environment variables from .env.local file
load_dotenv()

agent = gmail_reader_agent()

emails = fetch_mail()

# print(emails)

task = gmail_todo(agent, emails)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    process=Process.sequential,
)

results = crew.kickoff()
print(results)