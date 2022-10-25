from alive_progress import alive_bar
import time

items= range(100)

with alive_bar(len(items))as bar:
    for item in items:
        bar()
        time.sleep(0.1)