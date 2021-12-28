from instabot import Bot
import os
import shutil


def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("imgs\{}".format(i))
        os.rename(remove_me, src)


def upload_post(i):

    bot = Bot()

    bot.login(username="denemebottest", password="1234567a")
    bot.upload_photo("1.jpg".format(i), caption="Caption for the post")


if __name__ == '__main__':
    # enter name of your image bellow
    image_name = "1.jpg"
    clean_up(image_name)
    upload_post(image_name)
