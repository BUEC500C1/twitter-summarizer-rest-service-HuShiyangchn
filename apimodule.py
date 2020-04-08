import tweepy
import wget
import os
import datetime
import configparser

#import urllib2

class twittercatch():

    def __init__(self):
        '''
        consumer_key = "5BPSMCofACuMtRLPEWM5RGQoO"
        consumer_secret = "oKr8gArD2uwgOz4cnFzw7JqmmMyX51o3oMOkl5fhWSR591Gs1F"
        access_token ="1227718321874669568-tjbyvDD73So1buu8Wx8kPKSJBj8GJb"
        access_token_secret="TceCoqwG0MtaaXDxjSSxPyCtGURSs4aMc4b5rMw2zTZJZ"
        '''
        config = configparser.ConfigParser()
        config.read("keys")
        consumer_key = config.get('auth', 'consumer_key').strip()
        consumer_secret = config.get('auth', 'consumer_secret').strip()
        access_token = config.get('auth', 'access_token').strip()
        access_secret = config.get('auth', 'access_secret').strip()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        self.api = tweepy.API(auth)

    def gettweets(self, topic):
        keyword = topic

        tweets = self.api.user_timeline(keyword , count=10, tweet_mode='extended')

        media_files = set()

        for status in tweets:
            media = status.entities.get('media', [])
            if(len(media) > 0):
                media_files.add(media[0]['media_url'])

        for media_file in media_files:
            wget.download(media_file)

        direct = os.getcwd()
        tweetdir = os.path.join(direct,'tweets')

        contentlist = []
        print(tweets)
        for tweet in tweets:
            if (tweet.created_at.date() == datetime.date.today()):
                contentlist.append(tweet.full_text)
                #fileobject.write('\n')
        for items in contentlist:
            print(items, end=' ')

        for i in range(len(contentlist)):
            filename = 'tweet%s.txt' %(i)
            filepath = os.path.join(tweetdir,filename)
            with open(filepath,'w') as fileobject:
                fileobject.write(contentlist[i])
                #for tweet in tweets:

'''
      def save_json(self,username):
            json_tweets = json.dumps(self.content,indent = 4)
            path = 'Json/'+username+'.json'
            with open(path, 'w') as outfile:
                outfile.write(json_tweets) 
                '''