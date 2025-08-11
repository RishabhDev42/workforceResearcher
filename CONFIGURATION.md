# Configuration Guide for Collaborators

This document provides step-by-step instructions for setting up the project and running it locally.

---

## Prerequisites

1. **Python**: Ensure Python 3.12.7 is installed.
2. **Conda**: Install Conda 24.11.3 for environment management.
3. **Git**: Install Git for version control.
4. **Ngrok**: Download and set up Ngrok for exposing local servers.

---

## Project Setup

### 1. Clone the Repository
Clone the project repository from GitHub:
```bash
git clone https://github.com/RishabhDev42/workforceResearcher
cd workforceResearcher
```

### 2. Create a Conda Environment
Create and activate a new Conda environment:
```bash
conda create -n slack-fastapi python=3.12.7 -y
conda activate slack-fastapi
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## Environment Variables

### 1. Create a `.env` File
Create a `.env` file in the root directory and add the following variables:
```dotenv
SLACK_BOT_TOKEN=<your_slack_bot_token>
SLACK_SIGNING_SECRET=<your_slack_signing_secret>
MONGO_URI=<your_mongo_uri>
OPENAI_API_KEY=<your_openai_api_key>
```

### 2. Exclude Sensitive Files
Ensure `.env` is listed in `.gitignore` to prevent committing sensitive information.

---

## Running the Application

### 1. Start the FastAPI Server
Run the application using Uvicorn:
```bash
uvicorn app.main:app --reload
```

### 2. Expose the Server with Ngrok
Start Ngrok to expose the local server:
```bash
ngrok http 8000
```
Copy the public URL provided by Ngrok and configure it in your Slack app.

---

## Slack App Configuration

1. Go to your Slack app's settings.
2. Set the **Request URL** for events to:
   ```
   <ngrok_url>/slack/events
   ```
3. Enable the necessary event subscriptions and bot permissions.

---

## Testing

1. Send a message in Slack containing the word "AI" to test the bot's response.
2. Verify the bot replies as expected.

---

## Additional Notes

- Use `conda deactivate` to exit the environment when done.
- For any issues, refer to the project README or contact the maintainer.