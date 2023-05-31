from instabot import Bot

my_bot = Bot()

my_bot.login(username="coolartinfo",password = "Ayla0830!")

my_bot.upload_photo(photo="download.png", caption="Hello World!")

my_bot.logout()

print("worked")