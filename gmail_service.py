from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.search import GmailSearch
from langchain_google_community.gmail.create_draft import GmailCreateDraft
from langchain_google_community.gmail.utils import (
        build_resource_service, get_gmail_credentials
    )

credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json"
)

# Now use these credentials instead of trying to get new ones
api_resource = build_resource_service(credentials=credentials)

# Here is the source code for this function
# https://api.python.langchain.com/en/latest/_modules/langchain_community/tools/gmail/search.html#GmailSearch

def fetch_mail():
    '''
    Fetch emails from gmail inbox

    Returns:
        list of dicts: Information from latest 10 emails 
    '''

    search = GmailSearch(api_resource=api_resource)

    emails = search.invoke("in:inbox")

    mails = []

    for email in emails:
        mails.append({
            "id": email["id"],
            "sender": email["sender"],
            "subject": email["subject"],
            "snippet": email["snippet"],
            })
        
    return mails
