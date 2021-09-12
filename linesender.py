from linebot import LineBotApi
from linebot.models import TextSendMessage
import schedule
import time
import tweepy

line_bot_api = LineBotApi('UUgWxP3ys64NJAjbIyDnR09MlFMn7juyXYOzHKWwzgd8KP/WE/2MIfMJ7/fteRfv0Mg2d6LzYLMMndqJneKg510vnrb786l3l/X/lpRxP64FIRUab/gY0i2ySELfszyhbsDtMBdVCY+68lXt1Xf8OQdB04t89/1O/w1cDnyilFU=')


CK = "ZRE294kunRZy5jqaPxpTjfb1F"
CS = "a7bnW2hclUg0pGTz1UTpFiNMcl4zvO0UCerJd3FlGRb8KIyqaG"
AT = "1317127647944531970-Y2dZmgSVe3cBETyLfGhH4UVxI9Zgli"
AS = "G2VhZuQr6j7b87poxS79xvpliNBHUKKlupea3ou7Darku"

auth = tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)

api = tweepy.API(auth)

Account = "NITNiCdormitory"




def menu_get():
    tweets = api.user_timeline(Account,count=1)
    for tweet in tweets:
        tweet_text = tweet.text

    message = tweet_text
    print("get text!")
    USER_ID = "U0516ffa38dfa24d3aab65cdb3fd4db77"
    messages = TextSendMessage(text = message)
    line_bot_api.push_message(USER_ID,messages = messages)
    print("ok")
def main():
    schedule.every(1).day.at("06:13").do(menu_get)
    schedule.every(1).day.at("11:26").do(menu_get)
    schedule.every(1).day.at("16:43").do(menu_get)
    schedule.every(1).day.at("21:00").do(menu_get)
    schedule.every(5).day.at("20:58").do(menu_get)
    print("start!")

    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()
