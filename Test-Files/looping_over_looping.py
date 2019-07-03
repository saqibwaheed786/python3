import json 
import requests
import webbrowser
import sched, time


r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)

print(packages_str)
print(packages_json["stream"])

url = packages_json["stream"]
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    for urls in url:
        address = (packages_json["stream"])
        if url == url:
            new=2;
            webbrowser.open(address,new=new)
            print('Video is running in browser')
            break
        elif url != url:
            break
        else:
            new=2;
            webbrowser.open(address,new=new)
    s.enter(10, 1, do_something, (sc,))

s.enter(10, 1, do_something, (s,))
s.run()
