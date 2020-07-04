from slack import WebClient
from wheretoeat import WhereToEatBot
import config

slack_web_client = WebClient(token=config.SLACK_ACCESS_TOKEN)

restaurant_bot = WhereToEatBot('#général')

message = restaurant_bot.get_message_payload()

slack_web_client.chat_postMessage(**message)



