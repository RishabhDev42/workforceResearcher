from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

load_dotenv()

slack_app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

@slack_app.event("message")
def handle_message_events(event, say):
    text = event.get("text", "")
    if "AI" in text:
        say(f"I detected AI in your message: '{text}'")

if __name__ == "__main__":
    handler = SocketModeHandler(slack_app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()