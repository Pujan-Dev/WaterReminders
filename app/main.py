

import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Its time to drink water",
            message="Drink timmer",
            app_icon="logo.ico",
            timeout=10
        )
        time.sleep(60*60)
