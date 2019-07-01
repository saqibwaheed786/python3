import json 
import requests
import webbrowser
import subprocess


r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)

print(packages_str)
print(packages_json["stream"])

url_num_list = ['stream']

def schedule_runner(url_list):
    url_num_list = 'http://rhbsr001.koe.wige.local/v1/Data?id=4711'
for urls in url_num_list:
    address = (packages_json["stream"])  
    if url_num_list == url_num_list:
        new=2;
        webbrowser.open(address,new=new)
        break
        
    elif url_num_list != url_num_list:
        new=2;
        webbrowser.open(address,new=new);
         
schedule_runner(url_num_list)
