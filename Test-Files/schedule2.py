import json 
import requests
import webbrowser
import time
from schedule import * 
import schedule
import subprocess

r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)

print(packages_str)
print(packages_json["stream"])

r = r
while r == r:
    break
    print("The End")
else:
    new=2;
    url=(packages_json["stream"])
    webbrowser.open(url,new=new);
    

def job():
    new=2;
    url=(packages_json["stream"])
    webbrowser.open(url,new=new);
    subprocess.call("taskkill /IM chrome.exe")
schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)


def go_through_urls(url_list):

    prev_url = 0
    for url in url_list:

        if prev_url == 0:
            prev_url = url

        elif prev_url != url:

            play_video()

