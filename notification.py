import time
from player import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!",
            message = "Python is the best!",
            timeout = 3
        )
        time.sleep(100)
