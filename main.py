import os
from dotenv import load_dotenv
from crewai import Crew, Process
from gmail_agent import gmail_reader_agent, email_drafter_agent
from gmail_service import fetch_mail
from tasks import gmail_todo, draft_email_task
from textwrap import dedent

# Load environment variables from .env file
load_dotenv()

# Set up the agents
analyzer_agent = gmail_reader_agent()
drafter_agent = email_drafter_agent()

# Fetch emails from inbox
emails = fetch_mail()

# Step 1: Analyze emails to categorize them
analysis_task = gmail_todo(analyzer_agent, emails)

# Step 2: Create a task for drafting responses ONLY to important emails
drafting_task = draft_email_task(
    agent=drafter_agent,
    analysis_results="{{analysis_task.output}}",  # This will be replaced with the actual output
    emails=emails
)

# Set up the crew with sequential tasks
crew = Crew(
    agents=[analyzer_agent, drafter_agent],
    tasks=[analysis_task, drafting_task],
    process=Process.sequential,
    verbose=False  # Show detailed output during execution
)

# Run the crew
results = crew.kickoff()

# Print the results
print(dedent("""
------------------------------------------
EMAIL ANALYSIS AND DRAFTING RESULTS
------------------------------------------
"""))
print(results)
