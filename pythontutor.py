'''
i am writing a Python Program, that get the URL store in json stream 
this URL play .mp4 video which on cloud(API). 
When i change the video id then current video will be stop and
play new video corresponding with the id, that will happened after first video 
will end. Check if video id 
will same play same video otherwise play corresponding id video.
how to write loop that paly video till end and check above condition.

importatn: how to write simple loop ? that play video till end 
and check if video url will same play same video if url is not same 
play new video till end. just simple loop. 
'''


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
while r != r:
    print("The End")
    break
else:
    new=2;
    url=(packages_json["stream"])
    webbrowser.open(url,new=new);
    

def job():
    new=2;
    url=(packages_json["stream"])
    webbrowser.open(url,new=new);
#    subprocess.call("taskkill /IM chrome.exe")
    
    
#schedule.every(20).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
