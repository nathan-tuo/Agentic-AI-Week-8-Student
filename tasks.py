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

def draft_email_task(agent, analysis_results, emails):
    return Task(
        description=dedent(f"""
            IMPORTANT: ONLY draft responses for emails categorized as "Urgent" or "Important" in the analysis. 
            DO NOT draft responses for emails categorized as "FYI" or "Spam/Marketing".
            
            Here is the analysis of emails:
            {analysis_results}
            
            And here are the original emails for reference:
            {emails}
            
            For each email categorized as "Urgent" or "Important", draft a response with:
            1. An appropriate greeting
            2. Clear and concise body addressing the key points
            3. Professional closing
            4. Your signature
            
            Format your response as follows for each important email:
            
            ---
            EMAIL ID: [ID of the email]
            TO: [Sender's email]
            SUBJECT: Re: [Original subject]
            
            [Your complete response here]
            ---
            
            If there are no emails categorized as "Urgent" or "Important", simply respond with:
            "No urgent or important emails requiring response."
            """),
            
        agent=agent,
        
        expected_output='''Professional email responses ONLY for emails categorized as "Urgent" or "Important",
        formatted with proper email structure including greeting, body, and closing. Each response will be tailored
        to the specific email and ready to send without further editing.'''
    )


