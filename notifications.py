import psutil
from plyer import notification
import math

# The maximum threshold for cpu usage can be modified here
max_usage_percent = 25

# Change the frequency of cpu usage checks here
cooldown = 10

while True:
    cpu_usage = math.floor(psutil.cpu_percent(3))

    if cpu_usage > max_usage_percent:
        notification.notify(
            title = 'CPU Usage Alert',
            message = 'Your CPU usage looks high. You should close out any unneeded processes to decrease energy consumption',
            app_icon = None,
            timeout = cooldown
        )
