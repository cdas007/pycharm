__author__ = 'chiranjitdas'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="lSPvE37Lmb7yi6OpA5EiYjXtl"
consumer_secret="YtRWvpH9iwrIad7vsZh2YjhzauGtDD3XM3qU3Q7iY9FFWy4ywH"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="346159391-6VFeuNC1W6lD5K4xfZucbDOaawpv4C6TArjeUOuZ"
access_token_secret="ywJYKvcKEDVApSypsVvTfdRU5HflnY0F0QHMw2N8TNVYQ"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])