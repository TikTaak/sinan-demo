# from dotenv import load_dotenv

# import os
# import requests
# import instaloader

# from .bot.bot import bot, admins
from .instagram import Instagram
from .database import Database
import time
import config

class Main(object):
    def main():
        instagram = Instagram()
        database = Database()

        while True:
            posts = instagram.fetch_data(config.TARGET_INSTAGRAM_USERNAME)
            ids = posts['mediaid']
            caption = posts['caption']
            for _ in range(len(ids)):
                database.add_post(ids[_], caption[_])
                
            time.sleep(1)
















# load_dotenv()
# ig = instaloader.Instaloader()
# print("load env data")
# INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
# INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# admins.send_message("login to instagram...")
# try:
#     ig.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
#     admins.send_message("login successful")
# except Exception:
#     admins.send_message(f"login failed with exception: {Exception}")
    
# ig.download_profile("cristiano", profile_pic_only=True)


# print("loading profile...")
# profile = instaloader.Profile.from_username(ig.context, 'lyrics.editz0')
# admins.send_message("main.py")
# print("Done.")
# result = [post.mediaid for post in profile.get_posts()]
# print(result)


# for post in profile.get_posts():
#     print(post.url)
    # caption = post.caption
    # print(caption)


















# INSTAGRAM_TOKEN = os.getenv('INSTAGRAM_TOKEN')

# USERNAME = "therock"

# res = requests.get(f"https://graph.instagram.com/me?fields=id,username&access_token={INSTAGRAM_TOKEN}")
# print(res.text)

# res = requests.get(f"https://graph.instagram.com/me/media?fields=id,caption&access_token={INSTAGRAM_TOKEN}")
# print(res.text)

# # _url = "https://graph.instagram.com/me/17841405309211844?fields=business_discovery.username(bluebottle){followers_count,media_count,media{comments_count,like_count}}&access_token="+INSTAGRAM_TOKEN
# # res = requests.get(_url)
# # print(res.text)

# res = requests.get(f"https://graph.instagram.com/v1/users/banksy/media/6433231553443510/?access_token={INSTAGRAM_TOKEN}")
# print(res.text)
