import json 
import requests
import webbrowser
import time
from apscheduler.schedulers.background import BackgroundScheduler

r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)

REFRESH_INTERVAL = 10 #seconds
scheduler = BackgroundScheduler()
scheduler.start()

print(packages_str)
print(packages_json["stream"])

REFRESH_INTERVAL = 10 #seconds
 
scheduler = BackgroundScheduler()
scheduler.start()
 
def main():
    # Call our function the first time
    myFunction()
 
    # then every 60 seconds after that.
    scheduler.add_job(myFunction, 'interval', seconds = REFRESH_INTERVAL)
 
    # main loop
    while True:
        time.sleep(1)
 
def myFunction():
    url = packages_json["stream"]
 #   print ("Calling this fucntion every %d seconds" % REFRESH_INTERVAL)
    for urls in url:
        address = (packages_json["stream"])
        if url == url:
            new=2;
            webbrowser.open(address,new=new)
            print('Video is running in browser')
            break
        elif url != url:
            break
if __name__ == "__main__":
    main()



    
            
                            
