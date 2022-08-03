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
            message = 'Your CPU usage looks high. You should close out any unneeded processes to decrease energy consumption',
            app_icon = None,
            timeout = 30
        )
