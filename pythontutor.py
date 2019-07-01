'''
I want to write a program for videos looping for example: 
My loop check the video URL if the video URL is == (equal to) 
video URL play the video and loop this video again and again.
If the video URL is != (not equal to Video URL) Current video URL 
stop and start the default video. 

in this python script, get the URL from json stream which are store in 
one of aws.
1:requests module use for get URL 
2:webbrowsr use for open URL
This is my code  
'''
import json 
import requests
import webbrowser

r = requests.get('http://rhbsr001.koe.wige.local/v1/Data?id=4711')
packages_json =r.json()
packages_str = json.dumps(packages_json, indent=2)

print(packages_str)
print(packages_json["stream"])

url_num_list = ['stream']

for urls in url_num_list:
    address = (packages_json["stream"])
    if url_num_list == url_num_list:
        new=2;
        webbrowser.open(address,new=new)
        break
        
    elif url_num_list != url_num_list:
        new=2;
        webbrowser.open(address,new=new);
         
