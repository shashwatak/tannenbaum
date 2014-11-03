#!/usr/bin/python
from twitter import TwitterStream, OAuth
from credentials import CONSUMER_KEY, CONSUMER_SECRET

ACCESS_TOKEN = "68374651-On3ObzwpFDGLuctRa1uk5ekFXTlYz3oDwW4efJigq"
ACCESS_TOKEN_SECRET = "eQGJ3piUtvtPYrAiW7HrMxxg6oGYjdEB5lHR1tioN3E0C"



class Economy:
  def run(self):
    stream = TwitterStream(auth=OAuth(ACCESS_TOKEN,
                                      ACCESS_TOKEN_SECRET,
                                      CONSUMER_KEY,
                                      CONSUMER_SECRET))
    tweets = stream.statuses.sample()
    for tweet in tweets:
      if "entities" in tweet:
        print [hashtag["text"] for hashtag in tweet["entities"]["hashtags"]]
      else:
        print "<invalid>"



if __name__ == '__main__':
  economy = Economy()
  economy.run()
