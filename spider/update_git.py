import requests
import webbrowser, time
web_page="https://github.com/FengChangqing01/Network-Programming"
api = "https://api.github.com/repos/FengChangqing01/Network-Programming"

"""get info"""
all_info = requests.get(api).json()
last_update = "2018-12-03T11:38:06Z"
cur_update = all_info['updated_at']

while True:
    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        last_update = cur_update
        webbrowser.open(web_page)
    print(cur_update)

    time.sleep(60)