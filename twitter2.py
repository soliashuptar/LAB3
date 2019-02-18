import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_data(acct, info):
    """
    (string, string) ->

    Function prints on the screen information from json file that user wants to get
    """
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})
    connection = urllib.request.urlopen(url, context=ctx)
    headers = dict(connection.getheaders())
    data = connection.read().decode()

    js = json.loads(data)

    for i in js['users']:
        print(i['name'])
        if info == "followers_count":
            print(i["followers_count"])
        elif info == "friends_count":
            print(i["friends_count"])
        elif info == "date of creation":
            print(i["created_at"])
        elif info == "id":
            print(i["id"])
        elif info == "screen_name":
            print(i["screen_name"])
        elif info == "location":
            print(i["location"])
        elif info == "url":
            print(i["url"])


if __name__ == "__main__":
    acct = input('Enter Twitter Account:')
    print(" ")
    print(["id", "location", "url", "followers_count", "date of creation", "screen_name"])
    info = input('Enter where you want to get:')
    print(get_data(acct, info))
