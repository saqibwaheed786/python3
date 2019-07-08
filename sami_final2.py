import json 
import requests
import webbrowser
import sched, time
import subprocess

r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json = r.json()
packages_str = json.dumps(packages_json, indent=2)

print(packages_str)
print(packages_json["stream"])

url = packages_json["stream"]

s = sched.scheduler(time.time, time.sleep)

while True:
    address = (packages_json["stream"])
    time.sleep(1)
    r1 = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
    packages_json = r1.json()
    url1 = packages_json["stream"]
    changed= url != url1
    if changed:
        address = (packages_json["stream"])
        subprocess.call("taskkill /IM chrome.exe")
        webbrowser.open(address,new=2)
        url=url1
    else:
        print('')
