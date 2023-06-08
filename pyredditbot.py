import os
import praw
import time
import pandas as pd
from datetime import datetime

#### Todays Date ####
date = str(datetime.today().date())
png = str(".jpg")
filename = date + png
foldername = str("Redditbot/")
# print(filename)
# print(date)
#### Keys and Login Info ####
redditbot = praw.Reddit(
    client_id = "7KF0txiFFmW-vmhybJLt3g",
    client_secret = "d1IUqAjcel3uOFE0O5jJhmSpCJk-Rw",
    user_agent = "My user agent",
    username = "Professional_Lead_94",
    password = "Valeria30!"
    )

#### Subreddit Bot will be posting to ####
subreddit = redditbot.subreddit("r/Sdghffs")

#### Caption and Picture ####

#### Pictures ####
if filename in os.listdir("Redditbot"):
    picture = filename
else:
    print("Try again you fuggin loser")

content = foldername + picture
#### Title/Artist name ####
df = pd.read_csv('artists.csv')
Caption = df[(df['Date'] == date)]["name"]

#### Uploading ####
upload = subreddit.submit_image(Caption, content)