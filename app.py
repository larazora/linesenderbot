from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from time import time

import tweepy
import schedule


app = Flask(__name__)

users = {}

line_bot_api = LineBotApi('UUgWxP3ys64NJAjbIyDnR09MlFMn7juyXYOzHKWwzgd8KP/WE/2MIfMJ7/fteRfv0Mg2d6LzYLMMndqJneKg510vnrb786l3l/X/lpRxP64FIRUab/gY0i2ySELfszyhbsDtMBdVCY+68lXt1Xf8OQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66d0d8178eb0f37284f761167b2abcd3')

CK = "ZRE294kunRZy5jqaPxpTjfb1F"
CS = "a7bnW2hclUg0pGTz1UTpFiNMcl4zvO0UCerJd3FlGRb8KIyqaG"
AT = "1317127647944531970-Y2dZmgSVe3cBETyLfGhH4UVxI9Zgli"
AS = "G2VhZuQr6j7b87poxS79xvpliNBHUKKlupea3ou7Darku"

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)

Account = "NITNiCdormitory"

User_ID = set()

def sendMessage():
    text = menu_get()
    messages = TextSendMessage(text=text)
    line_bot_api.push_message(User_ID, messages=messages)




def menu_get():
    tweets = api.user_timeline(Account,count=1)
    for tweet in tweets:
        tweet_text = tweet.text
    return tweet_text
    #print(tweet_text)



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    userId = event.source.user_id

    if event.message.text == "勉強開始":
        reply_message = "計測を開始しました。"

        if not userId in users:
            users[userId] = {}
            users[userId]["total"] = 0
            User_ID.append(userId)


        users[userId]["start"] = time()
    elif event.message.text == "勉強終了":
        end = time()
        difference = int(end - users[userId]["start"])
        users[userId]["total"] += difference
        if difference >= 3600:
            hours = difference//3600
            minutes = difference//60
            seconds = difference%60
            total = users[userId]["total"]
            totalhours = total//3600
            totalminutes = total//60
            totalseconds = total%60
            reply_message = f"ただいまの勉強時間は{hours}時間{minutes}分{seconds}秒です。お疲れさまでした。これまでの総合勉強時間は{totalhours}時間{totalminutes}分{totalseconds}秒です。"
        elif difference >= 60:
            minutes = difference//60
            seconds = difference%60
            total = users[userId]["total"]
            totalhours = total//3600
            totalminutes = total//60
            totalseconds = total%60
            reply_message = f"ただいまの勉強時間は{minutes}分{seconds}秒です。お疲れさまでした。これまでの総合勉強時間は{totalhours}時間{totalminutes}分{totalseconds}秒です。"
        else:
            seconds = difference
            total = users[userId]["total"]
            totalhours = total//3600
            totalminutes = total//60
            totalseconds = total%60
            reply_message = f"ただいまの勉強時間は{seconds}秒です。お疲れさまでした。これまでの総合勉強時間は{totalhours}時間{totalminutes}分{totalseconds}秒です。"


    else:
        reply_message = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message))

def main():
    schedule.every(1).day.at("06:13").do(sendMessage)
    schedule.every(1).day.at("11:26").do(sendMessage)
    schedule.every(1).day.at("16:43").do(sendMessage)
    schedule.every(1).minutes.do(sendMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    app.run()
    main()
