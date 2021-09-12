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




def menu_get():
    tweets = api.user_timeline(Account,count=1)
    for tweet in tweets:
        tweet_text = tweet.text
    #print(tweet_text)

    messages = TextSendMessage(text=tweet_text)
    line_bot_api.push_message(user_id, messages=messages)





def main():

    schedule.every(1).minutes.do(menu_get)


if __name__ == "__main__":
    main()
