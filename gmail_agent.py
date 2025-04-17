from crewai import Agent, LLM
from textwrap import dedent

def gmail_reader_agent():
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",  # This is the correct format with groq/ prefix
        temperature=0.7
    )
    
    agent = Agent(
        role="Senior Email Analyst",
        goal="Analyze my email inbox; filter useless emails from important/must-respond-to emails",
        backstory=dedent('''As a Senior Email Analyst, you have an extensive background in analyzing email sentiments and
                  content. You are able to decipher whether an email is SPAM, such as newsletters, colleges, or NOT SPAM such as
                  a scheduled meeting, deadline, etc. Your expertise lies in analyzing the importance of an email and
                  indicating whether an email is worth replying to or not.'''),
        llm=llm,
    )
        
    return agent