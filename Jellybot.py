import praw
from imageai.Detection import ObjectDetection
#[TODO: Personfix: Fix the import of objectdetection to the right version]

#reddit login for API
reddit = praw.Reddit(   client_id="------------------------",
                        client_secret="------------------------",
                        password="------------------------",
                        user_agent="Jellybot was created by u/oocryoo",
                        username="------------------------"
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
                #############################################
                #[TODO: Fix this code block after the import update is fixed]
                submission = comment.submission
                url = submission.url

                detector = ObjectDetection()

                model_path = url
                input_path = url
                output_path = url

                detector.setModelTypeAsTinyYOLOv3()
                detector.setModelPath(model_path)
                detector.loadModel()
                detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

                for eachItem in detection:
                    print(eachItem["name"] , " : ", eachItem["percentage_probability"])
                #############################################

                reply = 'Thnx for using Jellybot! ATM were still working on the repost detection functions.'
                comment.reply(reply)
                print('posted')
        except:
            print('to frequent')