from dotenv import load_dotenv

import os
# import requests
import instaloader

from .bot.bot import admins

class Instagram(object):
    ig = None
    is_login = False
    user = ""
    
    def __init__(self):
        load_dotenv()
        self.ig = instaloader.Instaloader()
        INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
        INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
        admins.send_message("login to instagram...")
        try:
            self.ig.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            admins.send_message("login successful")
            self.is_login = True
        except Exception:
            admins.send_message(f"login failed with exception: {Exception}")
            
    def fetch_data(self, user):
        if self.is_login:
            self.user = user
            profile = instaloader.Profile.from_username(self.ig.context, user)
            return {
                "mediaid":[post.mediaid for post in profile.get_posts()],
                "caption":[post.caption for post in profile.get_posts()],
            }