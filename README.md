# twitter-summarizer-rest-service-HuShiyangchn
## Structure ##
1. Process Part </br>
   apimodule.py--get the tweets </br>
   convert.py --transfer the text file into image then combine the image into a video. </br>
2. Rest Part</br>
   Run the flask app then run the first part to generate a video by typying the url.
## Result ##
Run python app.py to start the flask application.
Then type curl http://127.0.0.1:5000/"username". The application will search for tweets of the "username" and produce the result automatically.</br>
![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-HuShiyangchn/blob/master/image/result.png)
## Run on AWS ##
1. Launch the instance with Unbuntu system which has python already. So we don't need to download python. Then download the .pem file.
2. Typing the command <p> ssh -i /path/key_pair.pem ubuntu@public_dns_name</p>
in terminal to link to the instance. Then install pip and virtualenv to create a virtual environment for our flaks application. The command should be like this
        <p>$ sudo apt-get upgrade</p>
        <p>$ sudo apt-get install python-pip</p>
        <p>$ pip install virtualenvwrapper</p>
        <p>$ virtualenv flask</p>
        <p>$ source /home/ubuntu/flask/bin/activate</p>
        <p>$ pip install flask<p>
3. Then we use sftp tool to upload our program:
    <p>$ sftp -i /path/key_pair.pem ubuntu@public_dns_name
    </p>$ lcd "local path of code"
    <p> $ put -r .<p>
    Then we can run the application in ssh:
    <p>$ nohup python3 app.py&</br>
    Then we can get the output at nohup.out file.
    By reading the file we can see the log of running flask service.<br>
    The snapshot of testing:<br>
    
    ![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-HuShiyangchn/blob/modified/image/test.png)
    
    ![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-HuShiyangchn/blob/modified/image/test1.png)
    
    ![image](https://github.com/BUEC500C1/twitter-summarizer-rest-service-HuShiyangchn/blob/modified/image/test2.png)
