from crewai import Agent, LLM
from textwrap import dedent

GROQ_API_KEY = ""  # Replace with your actual Groq API key
def gmail_reader_agent():
    llm = LLM(
        api_key=GROQ_API_KEY,  # groq API Key here
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

def email_drafter_agent():
    llm = LLM(
        api_key=GROQ_API_KEY,  # groq API Key here
        model="groq/llama-3.3-70b-versatile",
        temperature=0.7
    )
    
    agent = Agent(
        role="Selective Email Responder",
        goal="Draft professional responses ONLY for important emails that require action",
        backstory=dedent('''You are a highly efficient email communication specialist who focuses exclusively on 
                  responding to important emails. You understand that your time is valuable and should not be wasted 
                  on spam, marketing messages, or FYI emails that don't require a response. You have an excellent 
                  ability to craft concise, effective responses to genuinely important communications.
                  
                  You prioritize emails marked as "Important" or "Urgent" by the email analyzer and ignore 
                  everything categorized as "Spam/Marketing" or "FYI". Your responses are professional, 
                  targeted to the specific needs of each important email, and designed to efficiently resolve
                  the matter at hand.'''),
        llm=llm,
    )
    
    return agent
