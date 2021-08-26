import tweepy as tw
import environment as env
import dbService as dbService


def main():

    linha = dbService.getLinhaMaisVendidaByMesAno(2019, 12)
    nomeLinha = linha[1].lower()
    print(nomeLinha)
    auth = tw.OAuthHandler(env.api_key, env.api_key_secret)
    auth.set_access_token(env.access_token, env.access_token_secret)

    api = tw.API(auth)

    query = "boticario&"+ "maquiagem" + " -filter:retweets"
    tweets = tw.Cursor(api.search, q=query).items(50)

    for tweet in tweets:
        print(tweet.text)
        print("")

main()