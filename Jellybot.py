import praw
from PIL import Image
import requests
from io import BytesIO

#reddit login for API
reddit = praw.Reddit(   client_id="======",
                        client_secret="="======",",
                        password="="======",",
                        user_agent="Jellybot was created by u/oocryoo",
                        username="="======","
                    )

print(reddit.user.me())

#Giving the subreddits that the bot is allowed to use [TODO: make it a array or a list or something lmao]
subreddit = reddit.subreddit('testingground4bots')

#Call to the bot
keyphrase = '!jellycheck'

# looks if the keyphrase is called in the comments
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        print('Comment found!')
        try:
            try:
                url = "https://www.gettyimages.pt/gi-resources/images/Homepage/Hero/PT/PT_hero_42_153645159.jpg"
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))

                # getting colors
                imgColor = Image.getcolors(img)

                print(imgColor)

                reply = 'Jellybot found the same post!'
                comment.reply(reply)
                print('posted, repost found')
            except:
                reply = 'Thnx for using Jellybot! ATM Jellybot cant find another post. So this is probally not a repost.'
                comment.reply(reply)
                print('posted, no repost found')
        except:
            print('to frequent')