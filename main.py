import tweepy as tw
import pandas as pd
import environment as env
import dbService as db


def main():

    linha = db.getLinhaMaisVendidaByMesAno(2019, 12)
    auth = tw.OAuthHandler(env.api_key, env.api_key_secret)
    auth.set_access_token(env.access_token, env.access_token_secret)

    api = tw.API(auth)

    query = "Boticario&"+ linha + " -filter:retweets"
    tweets = tw.Cursor(api.search, q=query).items(1)

    for tweet in tweets:
        print(tweet.text)
        print("")

main()