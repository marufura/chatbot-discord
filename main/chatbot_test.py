import sys
import requests
import urllib.parse
import config.chatbot_config as config


class ChatBotException(Exception):
    pass


class ChatBot(object):

    def __init__(self, api_key, api_endpoint):
        self.api_key = api_key
        self.api_endpoint = api_endpoint

    def get_reply_message(self, message):
        message_encoded = urllib.parse.quote(message)
        params = {
            'key': self.api_key,
            'message': message_encoded
        }

        response = requests.get(self.api_endpoint, params=params)
        if response.status_code != requests.codes.ok:
            raise ChatBotException('Invalid status code: %d' % response.status_code)

        result_json = response.json()
        return result_json["result"]


# this is for test
if __name__ == '__main__':
    chat_bot = ChatBot(api_key=config.api_key, api_endpoint=config.api_endpoint)
    print(chat_bot.get_reply_message(sys.argv[1]))
