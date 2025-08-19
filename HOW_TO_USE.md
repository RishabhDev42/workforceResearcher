## How to Use Workforce Researcher

### 1. Install Python and pip

- Download and install Python from [python.org](https://www.python.org/downloads/).
- During installation, check the box “Add Python to PATH”.
- pip (Python’s package manager) is included with Python.

### 2. Download the Project

- Download or clone the [project files](https://github.com/RishabhDev42/workforceResearcher) to your computer.

### 3. Install Project Requirements

- Open the Command Prompt.
- Navigate to the project folder.
- Run:
  ```
  pip install -r requirements.txt
  ```

### 4. Set Up Environment Variables

- Create a file named `.env` in the project folder.

#### Get your OpenAI API Key

- Sign up or log in at [OpenAI Platform](https://platform.openai.com/).
- Go to [API Keys](https://platform.openai.com/api-keys).
- Click “Create new secret key” and copy the key.
- For more help, see [OpenAI API Key documentation](https://platform.openai.com/docs/quickstart/account-setup).

#### Get your MongoDB URI

- Sign up or log in at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
- Create a new cluster (free tier is available).
- In your cluster, click “Connect” → “Connect your application”.
- Copy the provided connection string (URI).
- For more help, see [MongoDB Atlas Getting Started](https://www.mongodb.com/docs/atlas/getting-started/).

#### Add your Slack tokens/secrets

- Follow Step 5 to create a Slack app and get the required tokens.

#### Example `.env` file

```dotenv
SLACK_BOT_TOKEN=<your_slack_bot_token>
SLACK_SIGNING_SECRET=<your_slack_signing_secret>
SLACK_APP_TOKEN=<your_slack_app_token>
MONGO_URI=<your_mongo_uri>
OPENAI_API_KEY=<your_openai_api_key>
```

Replace the placeholders with your actual credentials.

### 5. Create a Slack App

- Go to [Slack API: Your Apps](https://api.slack.com/apps) and create a new app.
- In your app, go to **Features > App Manifests**.
- Paste the following manifest into the editor:

```json
{
    "display_information": {
        "name": "workforceResearcher"
    },
    "features": {
        "app_home": {
            "home_tab_enabled": true,
            "messages_tab_enabled": false,
            "messages_tab_read_only_enabled": true
        },
        "bot_user": {
            "display_name": "workforceResearcher",
            "always_online": true
        }
    },
    "oauth_config": {
        "scopes": {
            "user": [
                "admin"
            ],
            "bot": [
                "app_mentions:read",
                "bookmarks:read",
                "calls:read",
                "canvases:read",
                "channels:history",
                "channels:join",
                "channels:read",
                "files:read",
                "groups:history",
                "groups:read",
                "im:history",
                "im:read",
                "mpim:history",
                "usergroups:read",
                "users:read",
                "chat:write.customize",
                "chat:write",
                "incoming-webhook"
            ]
        }
    },
    "settings": {
        "event_subscriptions": {
            "bot_events": [
                "message.channels",
                "message.groups",
                "message.im",
                "message.mpim"
            ]
        },
        "interactivity": {
            "is_enabled": true
        },
        "org_deploy_enabled": false,
        "socket_mode_enabled": true,
        "token_rotation_enabled": false
    }
}
```

- Click **Next** and follow the prompts to finish setting up your app.
- Install the app to your workspace.

#### Where to find your tokens and secrets

- **Bot Token**: Go to your app’s **OAuth & Permissions** page. Under **Bot User OAuth Token**, copy the token (starts with `xoxb-`).
- **Signing Secret**: Go to **Basic Information** in your app settings. Under **App Credentials**, copy the **Signing Secret**.
- **App Token**: Go to **Basic Information** > **App-Level Tokens**. Create a new token with the `connections:write` scope if needed, then copy the token (starts with `xapp-`).

Add these values to your `.env` file as shown in Step 4.

### 6. Run the Slack Bot

- In the Command Prompt, run:
  ```
  python app/main.py
  ```
- The bot will now monitor Slack and save relevant messages to your MongoDB cluster.

### 7. Analyze the Data

- Open the Jupyter Notebook at `analysis/Text Analysis SlackBot Application.ipynb`.
- Run all cells to generate CSV files with the analysis results.

### 8. View the Dashboard

- Move the generated CSV files into the `text-sentiment-dashboard/data` folder.
- In the Command Prompt, navigate to the `text-sentiment-dashboard` folder.
- Run:
  ```
  streamlit run Home.py
  ```
- Open [http://localhost:8501](http://localhost:8501) in your browser to view the dashboard.