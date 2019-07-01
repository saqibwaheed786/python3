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
    elif url != url:
        new=2;
        webbrowser.open(address,new=new)
        break
    
        
        
    
    
        


         
