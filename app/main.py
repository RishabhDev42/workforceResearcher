from fastapi import FastAPI, Request
from slack_bolt.adapter.fastapi import SlackRequestHandler
from slack_bolt import App as SlackApp
import os
from dotenv import load_dotenv

load_dotenv()

slack_app = SlackApp(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)
handler = SlackRequestHandler(slack_app)

app = FastAPI()

# Slack event listener
@slack_app.event("message")
def handle_message_events(event, say):
    text = event.get("text", "")
    if "AI" in text:  # simple placeholder filter
        say(f"I detected AI in your message: '{text}'")

# Slack endpoint for events
@app.post("/slack/events")
async def slack_events(req: Request):
    return await handler.handle(req)