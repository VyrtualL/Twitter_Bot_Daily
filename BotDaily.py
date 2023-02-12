import tweepy
import schedule
import time
import random
import os

consumer_key = 
consumer_secret =
access_token = 
access_token_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

def post_tweet(text):
    api.update_status(text)
    
def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

def random_image():
    x = random.randint(0,500)
    y = str(x)
    if x < 10:
        return '000' + y + '.jpg'
    if x >= 10 and x < 100:
        return '00' + y + '.jpg'
    if x >= 100:
        return '0' + y + '.jpg'

def true():
    a = random_image()
    fileName = "/Users/Desktop/Bot/" + a
    if (os.path.isfile(fileName)==True):
        return a
    else:
        l = list(a)
        l[4] = '.'
        l[5] = 'p'
        l[6] = 'n'
        l[7] = 'g'
        a = "".join(l)
        return a

    
def finish():
    b = true()
    upload_media('', b)


schedule.every().day.at("00:00").do(finish)


schedule.every().day.at("04:00").do(finish)


schedule.every().day.at("08:00").do(finish)


schedule.every().day.at("12:00").do(finish)

schedule.every().day.at("16:00").do(finish)

schedule.every().day.at("20:00").do(finish)


while True:
    schedule.run_pending()
    time.sleep(1)
