import os
from os import path

from . import misc
from slack import WebClient
from slack.errors import SlackApiError


class Messenger:
    client = WebClient(token=misc.read_json(
        path.join(os.getcwd(), 'slack.json')
    )['SLACK_API_TOKEN'])

    @staticmethod
    def post(message, channel='#ркс-отчеты'):
        try:
            response = Messenger.client.chat_postMessage(
                channel=channel,
                text=message
            )
        except SlackApiError as e:
            assert e.response["ok"] is False
            assert e.response["error"]
            print(f"Got an error: {e.response['error']}")
