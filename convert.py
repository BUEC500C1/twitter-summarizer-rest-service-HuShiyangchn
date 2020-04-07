import os,queue
import subprocess
import time, threading
queue = queue.Queue()

#def text2video():
    #i = queue.get()
direct = os.getcwd()
tweetdir = os.path.join(direct,'tweets')
files = os.listdir(tweetdir)
imagepath = os.path.join(direct,'tweetimages')
num = 0
for items in files:
    print(items)
for items in files:
    with open(tweetdir + '/' +items) as file_object:
        #content = file_object.read()
        convert='ffmpeg -y lavfi -i color=c=white:s=1920x1080:d=0.5 -vf \
        "drawtext=fontfile=/path/to/font.ttf:fontsize=20: \
        fontcolor=black:x=(w-text_w)/2:y=(h-text_h)/2:textfile=%s/%s" \
        -frames:v 1 %s/image%03d.png' %(tweetdir, items, imagepath, num)
        os.system(convert)
        num = num + 1
        with open('input.txt','a') as inputfile:
            inputfile.write('%s/%s\n'%(tweetdir, items))
            inputfile.write('duration 3\n')
        
#subprocess.call(convert,shell = True)

#image2video
convertvideo = 'ffmpeg -loop 1 -f image2 -i '+ imagepath+'/image%03d.png -vcodec libx264 -r 10 -t 30 tweetdaily.mp4' 
os.system(convertvideo)

''' 
    queue.task_done()

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=text2video)
        t.daemon=True 
        t.start()

    time.sleep(3)
    for i in range(10):
        queue.put(i)

    queue.join()  
    '''