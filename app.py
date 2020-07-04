import logging
import config
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from wheretoeat import WhereToEatBot

app = Flask(__name__)

slack_events_adapter = SlackEventAdapter(config.SLACK_EVENTS_TOKEN, "/slack/events", app)
slack_web_client = WebClient(config.SLACK_ACCESS_TOKEN)


def choose_restaurant(channel):
    wheretoeat = WhereToEatBot(channel)

    message = wheretoeat.get_message_payload()

    slack_web_client.chat_postMessage(**message)


def choose_yelp_restaurant(channel):
    wheretoeat = WhereToEatBot(channel)

    message = wheretoeat.get_yelp_message_payload()

    slack_web_client.chat_postMessage(**message)


@slack_events_adapter.on("message")
def message(payload):
    event = payload.get("event", {})

    text = event.get("text")

    # if "where to eat" in text.lower():
    if "where to eat" in text.lower():
        channel_id = event.get("channel")

        return choose_restaurant(channel_id)

    elif "find me another place in yelp" in text.lower():
        logger.debug("Yelp hit")
        channel_id = event.get("channel")

        return choose_yelp_restaurant(channel_id)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    app.run(host='0.0.0.0', port=3000)
