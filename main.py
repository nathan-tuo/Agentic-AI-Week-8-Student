
from gmail_agent import Gmail_Agent
from tasks import Agent_Task

agent = Gmail_Agent.gmail_reader_agent()

task = Agent_Task.gmail_todo(agent, emails)

