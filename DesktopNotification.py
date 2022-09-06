import time
from plyer import notification

if __name__ =="__main__":
    while True:
        notification.notify(
            title = "NOTIFICATION!!!",
            message = "Cxnrd first relax!",
            timeout = 300
        )
        time.sleep(3600)
