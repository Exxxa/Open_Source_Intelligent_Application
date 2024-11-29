import http.client
def twitterpost(post):
    conn = http.client.HTTPSConnection("twitter241.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "08447beffamshd4f052f17c2317ep1fa7f6jsn10b0515b6fc8",
        'x-rapidapi-host': "twitter241.p.rapidapi.com"
    }

    conn.request("GET", f"/tweet?pid={post}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    responce = data.decode("utf-8")
    return responce

def instascrape(user):
    conn = http.client.HTTPSConnection("instagram-scraper-api2.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "08447beffamshd4f052f17c2317ep1fa7f6jsn10b0515b6fc8",
        'x-rapidapi-host': "instagram-scraper-api2.p.rapidapi.com"
    }

    conn.request("GET", f"/v1/info?username_or_id_or_url={user}&include_about=true&url_embed_safe=true", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def redditscrape(user):

    conn = http.client.HTTPSConnection("reddit-scraper2.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "08447beffamshd4f052f17c2317ep1fa7f6jsn10b0515b6fc8",
        'x-rapidapi-host': "reddit-scraper2.p.rapidapi.com"
    }

    conn.request("GET", f"/user_info?user=https%3A%2F%2Fwww.reddit.com%2Fuser%2F{user}%2F", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def tiktokscrape(user):
    conn = http.client.HTTPSConnection("tiktok-api23.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "08447beffamshd4f052f17c2317ep1fa7f6jsn10b0515b6fc8",
        'x-rapidapi-host': "tiktok-api23.p.rapidapi.com"
    }

    conn.request("GET", f"/api/user/info?uniqueId={user}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))