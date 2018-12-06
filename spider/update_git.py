import requests
import webbrowser, time
web_page="https://github.com/FengChangqing01/Network-Programming"
api = "https://api.github.com/repos/FengChangqing01/Network-Programming"


last_update = None
while True:
    """get info"""
    all_info = requests.get(api)
    try:
        all_info.raise_for_status()
    except Exception as exc:
        print("There was a problom: %s"%(exc))
        continue
    cur_update = all_info.json()['updated_at']

    if not last_update:
        last_update = cur_update

    if last_update < cur_update:
        last_update = cur_update
        webbrowser.open(web_page)
        print(cur_update)

    time.sleep(6)