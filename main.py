import psutil
import os
from plyer import notification
import math
import time

while True:
    cpu_usage = math.floor(psutil.cpu_percent(3))

    if cpu_usage > 25:
        notification.notify(
            title = 'CPU Usage Alert',
            message = str(cpu_usage),
            app_icon = None,
            timeout = 2
        )
        time.sleep(5)
