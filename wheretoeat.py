# import random library to choose an item from the array at random
import random


class WhereToEatBot:
    # Creating default text of the Slack message
    DEFAULT_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "WhereToEatBot suggests...\n\n"
            ),
        },
    }

    RESTAURANTS = [
        "Pères Populaires",
        "Japanese",
        "Italian",
        "Pizza",
        "Bo-bun",
        "Boulangerie",
        "Couscous",
    ]

    def __init__(self, channel):
        self.channel = channel

    # Select a random restaurant from the RESTAURANTS global list.
    # Then return the crafter slack payload with the restaurant name.
    def select_restaurant(self):
        restaurant = random.choice(self.RESTAURANTS)
        reply = f"{restaurant}"

        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": reply
            }
        },

    # Craft and return the entire message payload as a dictionary
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.DEFAULT_BLOCK,
                *self.select_restaurant(),
            ]
        }
