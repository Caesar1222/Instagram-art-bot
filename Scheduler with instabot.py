from instabot import Bot
from datetime import datetime
import os
import time 
bot = Bot()
bot.login()
time.sleep(5)
### Todays Time ###
# print(datetime.today())

k = []
with open("captions.txt") as pp:
        g = pp.readlines()
        for x in g:
            k.append(x[:-1].split(" ", 1)[0]) 
for filex in os.listdir("instabot"):
 
    if filex not in k:
        with open("captions.txt", "a") as pf:
            caption = input('caption: ')
            pf.write(filex)
            pf.write(" ")
            pf.write(caption)
            pf.write("\n")

with open("captions.txt") as fp:
    b = fp.readlines()
    for f in b:
        try:
            post,capx = f.split(" ",1)
            if post[:10] == str(datetime.today().date()):
                bot.upload_photo(post,capx)
        except:
            pass
bot.logout()