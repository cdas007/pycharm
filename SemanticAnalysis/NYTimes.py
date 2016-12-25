__author__ = 'chiranjitdas'
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# The consumer key and the consumer secret will be generated from the app
consumer_key = "Oj3u5eQkJ0lnda6vX0pqqKuNe"
consumer_secret = "MDTyZBSwe8JX8tsMpvzZZfyWoYty1gdISFnLibYh6dIJ4KnuRV"

# Access Token and the access key from the app page
access_token = "346159391-o4BYetpSRYMdKWV5VtAnTRKfw7JtOkzJa5P1Uvjt"
access_secret = "JVLw3wU66B3924E7hEZS9UkiHK84MedJ5znkoJZ0rBNCO"

class StdOutListener(StreamListener):

    """ A Listener handles all the tweets
    """

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '_main_':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_secret)

    stream = Stream(auth, l)
    stream.filter(track=['basket'])

