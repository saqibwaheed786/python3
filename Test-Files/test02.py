import json 
import requests
import webbrowser
import time
from schedule import * 
import schedule
import subprocess
# if all urls ar like http://rhbsr001.koe.wige.local/v1/Data?id="number"

# ! then skip that below !
r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)

print(packages_str)
print(packages_json["stream"])
# ! end skip !

# to here
# and fill the numbers like 4711, 4712
url_num_list = ['4711', 
                '4711', 
                '4713']


def schedule_runner(url_list):
    prev_url = ''
    # go through every url with a loop, skip the next if it's the same
    # as the previous
    # in our example it should go to example.com, skip the 
    # following example.com and go to example1.com
    prev_url_num = ''
    for number in url_num_list:
        address = 'http://rhbsr001.koe.wige.local/v1/Data?id=' + number
        if prev_url_num != number:
            new=2;
            webbrowser.open(address,new=new);
            # I dont know if I use schedule here correctly
            #kill the process after 10 sec
            time.sleep(10)
            subprocess.call("taskkill /IM chrome.exe")
            prev_url_num = number

schedule_runner(url_num_list)
