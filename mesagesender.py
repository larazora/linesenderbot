import os
from os.path import join, dirname
from dotenv import load_dotenv

from linebot import LineBotApi
from linebot.models import TextSendMessage

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

channel_access_token = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
user_id = os.environ.get('USER_ID')

line_bot_api = LineBotApi(channel_access_token)




def sendMessage(message):

    messages = TextSendMessage(text=message)
    line_bot_api.push_message(user_id, messages=messages)


if __name__ == "__main__":
    print("メッセージを入力してください")
    message = input()
    sendMessage(message)
    print("メッセージを送信しました")
