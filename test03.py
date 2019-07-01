'''
I want to write a program for videos looping for example: 
My loop check the video URL if the video URL is == (equal to) 
video URL play the video and loop this video again and again.
If the video URL is != (not equal to Video URL) video  
stop and start the default video.

Note
python module webbrowser not working in this site
'''
import webbrowser

url = 'https://www.youtube.com/watch?v=FLV1z9BWvyc'

for urls in url:
    address = url
    if url == url:
        #open the url in browser
        new=2;
        webbrowser.open(address,new=new)  
        #play the video till end when video will end then 
        #check loop again 
        #if URL (not equal) play default video
        
    '''
actually below script is the main script which i want to execute
just i want to solve the IF statement in this script otwise my script
is working on my side

import json for json stream
request module is for request
webbrowser for open URL


        
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
        
        
    '''
        
        
    
    
        


         
