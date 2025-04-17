from crewai import Task

class Agent_Task():
  def gmail_todo(agent, emails):
    return Task(
            description=f'''Analyze Gmail inbox to categorize and prioritize emails, identifying which messages require attention
            and which can be ignored. The agent will scan through emails, classifying them as important (meetings, deadlines,
            personal communications) or non-important (newsletters, marketing, automated notifications). For important emails,
            the agent will highlight action items, deadlines, and response requirements. This task helps users efficiently manage
            their inbox by focusing on what matters most, reducing email overload, and ensuring critical communications don't get missed.

            Here are the emails that I am providing to you:
            {emails}''',

            agent=gmail_agent,

            expected_output='''A categorized list of emails with priority levels, response recommendations, and suggested actions
            for each important message. The output should identify which emails can be safely archived or deleted and which require immediate attention.''')


