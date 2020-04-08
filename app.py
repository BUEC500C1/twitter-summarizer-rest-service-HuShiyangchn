import os
import subprocess
import time, threading
import queue
from flask import Flask, render_template, flash, redirect, url_for, Markup, send_file, send_from_directory

#from flask.restful import reqparse, abort, Api, Resource
from twassemble import twitter_assemble

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

#api = restful.Api(app)
queue = queue.Queue()

'''
@app.route('/watchlist2')
def watchlist_with_static():
    return render_template('watchlist_with_static.html')

# register template global function
@app.template_global()
def bar():
    return 'Clik the link blew to create the video.'

@app.route("/")
def index():
    return render_template('index.html')

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

'''
@app.route('/<twittertopic>')
def download_file(twittertopic):
    twitter_assemble(twittertopic)
    directory = os.getcwd().join('static')
    filename = 'tweetdaily'
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)


#curl http://127.0.0.1:90/boston
'''
#import text_to_image
def text2video():
#text2image
    convert_message = "Convert to video"
    i = queue.get()
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
    convertvideo = 'ffmpeg -loop 1 -y image2 -i '+ imagepath+'/image%03d.png -vcodec libx264 -r 10 -t 10 stastic/tweetdaily.mkv' 
    os.system(convertvideo)
    queue.task_done()
'''


'''
if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=text2video)
        t.daemon=True 
        t.start()

    time.sleep(3)
    for i in range(10):
        queue.put(i)

    queue.join()    

threads = []
t1 = threading.Thread(target=text2video)
threads.append(t1)
t2 = threading.Thread(target=text2video)
threads.append(t2)
t3 = threading.Thread(target=text2video)
threads.append(t3)
t4 = threading.Thread(target=text2video)
threads.append(t4)
t5 = threading.Thread(target=text2video)
threads.append(t5)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
        print('thread %s is running...' % threading.current_thread().name)
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
    print ("all over %s" %time.ctime())
'''
