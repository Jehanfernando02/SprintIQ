# SprintIQ
A side project I'm building to solve a problem I've seen firsthand — engineering teams using GitHub, Jira, and Slack separately but never having a single place that connects everything together.
The idea is simple: you ask a question like "why is the payment feature delayed?" and instead of manually checking three tools, SprintIQ figures it out for you by looking at commit history, open tickets, and Slack conversations.
## What it does
- Connects to GitHub, Jira, and Slack
- Builds a live picture of what's happening across the project
- Lets you ask questions in plain English and get actual answers with evidence
- Detects blockers before they turn into bigger problems
- Shows a dashboard with sprint health, overdue work, and PR status
## Tech
Backend is FastAPI with Python. Frontend is React with TypeScript. For the AI side, I'm using LangGraph to coordinate multiple agents — each one responsible for a different tool. Knowledge connections between developers, tickets, and blockers are stored in Neo4j. Regular project data goes into PostgreSQL.