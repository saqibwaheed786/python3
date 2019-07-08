'''
first get request and and print it which is already done.
Then start loop if stream is default.play the stream 
Otherwise if stream is not equal to default stream
close the browser and reopen the browser.
And play new stream in browser
loop above condition ever 1 second please help me how can I write this?
i will be very thankfull to you

'''
import json 
import requests
import webbrowser
import sched, time

r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)
print(packages_str)
print(packages_json["stream"])
#above get the request and print it
stream = packages_json["stream"]
print(packages_str)
print(packages_json["stream"])
stream = packages_json["stream"]
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
for streams in stream:
                address = (packages_json["stream"])
                if stream == stream:
                        new=2;
                        webbrowser.open(address,new=new)
                        break
                else: url != url
                subprocess.call("taskkill /IM chrome.exe")
                new=2;
                webbrowser.open(address,new=new)
                s.enter(10, 1, do_something, (sc,))
                s.enter(10, 1, do_something, (s,))
s.run()  
