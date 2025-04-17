from crewai import Task
from textwrap import dedent

def gmail_todo(agent, emails):
    return Task(
        description=dedent(f"""
            Analyze the following emails and categorize them into:
            1. Urgent - Needs immediate response
            2. Important - Should respond soon
            3. FYI - No response needed
            4. Spam/Marketing - Can be ignored
            
            For each email, provide:
            - Category
            - Brief reason for categorization
            - Suggested response approach (if applicable)
            
            Here are the emails to analyze:
            {emails}
            """),


            agent=agent,

            expected_output='''A categorized list of emails with priority levels, response recommendations, and suggested actions
            for each important message. The output should identify which emails can be safely archived or deleted and which require immediate attention.''')


