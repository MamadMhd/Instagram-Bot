from instabot import Bot
import os

def run_bot(username, password, target_hashtags):
    bot = Bot()
    try:
        bot.login(username=username, password=password)
        hashtags = target_hashtags.split(',')
        for hashtag in hashtags:
            bot.like_hashtag(hashtag.strip())
        return "Success"
    except Exception as e:
        return str(e)
    finally:
        bot.logout()
