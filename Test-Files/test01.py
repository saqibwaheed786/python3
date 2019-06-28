import json 
import requests
import webbrowser

new=2;


r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')

packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)

print(packages_str)
print(packages_json["stream"])

if r == r:
    print(r)
else:
    print(packages_json["stream"])
    
    
url=(packages_json["stream"])
webbrowser.open(url,new=new);
