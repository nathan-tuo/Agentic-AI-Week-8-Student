# Gmail Agent with CrewAI and Grok

This project implements an intelligent Gmail management system using CrewAI, Grok, and the Gmail API. The system uses specialized agents to search, analyze, and summarize emails using natural language commands.

## Features

- Multiple specialized agents powered by Grok's Mixtral-8x7b model:
  - Email Searcher: Finds relevant emails based on queries
  - Email Analyzer: Analyzes communication patterns
  - Email Summarizer: Creates concise email summaries
- Task-based workflow using CrewAI
- OAuth2 authentication with token persistence
- Natural language email interactions

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Google Cloud Project:
   - Go to the [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select an existing one
   - Enable the Gmail API
   - Create OAuth 2.0 credentials (Desktop application)
   - Download the credentials and save as `credentials.json` in the project root

3. Set your Grok API key as an environment variable:
```bash
export GROQ_API_KEY=your-grok-api-key
```

## Project Structure

- `agents.py`: Defines specialized Gmail agents using CrewAI and Grok
- `tasks.py`: Defines email-related tasks for the agents
- `main.py`: Main script that orchestrates the agents and tasks
- `requirements.txt`: Project dependencies
- `.env`: Configuration file
- `credentials.json`: Google OAuth credentials (you need to provide this)
- `token.pickle`: Persisted authentication token (generated automatically)

## Usage

Run the main script:
```bash
python main.py
```

The script demonstrates three main capabilities:
1. Searching for important emails
2. Analyzing email communication patterns
3. Summarizing emails with specific criteria

## How It Works

1. The system uses CrewAI to create specialized agents powered by Grok's Mixtral-8x7b model
2. Each agent has specific roles and goals:
   - Email Searcher focuses on finding relevant emails
   - Email Analyzer examines communication patterns
   - Email Summarizer creates concise summaries
3. Tasks are assigned to appropriate agents
4. The crew orchestrates the agents to work together

## Security Note

- Never commit your `credentials.json`, `token.pickle`, or expose your Grok API key
- Keep your API keys and tokens secure
- Follow OAuth2 best practices for token management 