# Workforce Researcher

A Python-based Slack bot that detects and analyzes conversations about technology, AI, automation, and their impact on jobs and the workforce.

## Features

- Monitors Slack channels for messages about job loss, automation, and technology-driven workforce changes
- Uses semantic similarity (OpenAI embeddings) for nuanced detection beyond keyword search
- Stores relevant messages in MongoDB for further analysis
- Ingests, processes and analyzes Slack messages in real-time.
- Rich reporting and insights on workforce trends

## Tech Stack

- Python
- Slack API (via `slack_sdk`)
- OpenAI API (for embeddings)
- MongoDB (via `pymongo`)

## Setup

1. **Clone the repository**
2. **Set up environment variables**
3. **Go through CONFIGURATION.md for detailed setup instructions**
4. **Alternatively follow the HOW_TO_USE.md guide for in-depth setup instructions for a non-technical audience**