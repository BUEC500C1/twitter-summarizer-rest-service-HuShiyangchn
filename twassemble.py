import apimodule as apm
import convert as convert

def twitter_assemble(topic):
    twitter = apm.twittercatch()
    keyword = topic
    twitter.gettweets(keyword)
    convert.text2video()

