from schedule import *
from time import *

def execute():

    notification.notify(
                title = "Stand Up Now!",
                message = f"Remember to stand up for a minute now!\n",
                app_icon = "man-standing-up.ico", # <a href="https://www.flaticon.com/free-icons/male" title="male icons">Male icons created by Freepik - Flaticon</a>
                timeout = 10,
            )

while True:

    every().hour.at(":00").do(execute)