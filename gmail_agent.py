from crewai import Agent

class Gmail_Agent():
  def gmail_reader_agent():
    return (
          Agent(
            role="Senior Email Analyst",
            goal="Analyze my email inbox; filter useless emails from important/must-respond-to emails",
            backstory='''As a Senior Email Analyst, you have an extensive background in analyzing email sentiments and
                      content. You are able to decipher whether an email is SPAM, such as newsletters, colleges, or NOT SPAM such as
                      a scheduled meeting, deadline, etc. Your expertise lies in analyzing the importance of an email and
                      indicating whether an email is worth replying to or not.''',
            llm=LLM(
                  model="groq/llama3-8b-8192", # Same model we used in Week 7
                  temperature=0.7
              ),  # The default is an open ai model/"gpt-4" ... which is not free so we use GROK
        )
    )