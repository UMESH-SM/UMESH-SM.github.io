import requests
from flask import render_template
from datetime import date

def req_news_data():
    url = ('http://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=8ecd5ce9df6c478a8ccae9b4a4817cf6')
        
    response = requests.get(url)
    res = response.json()
    art = res['articles']
    num = len(art)
    titles = []
    urls = []
    descriptions = []
    sources = []
    dateTime = []
    image_urls = []
    chars = ['T','Z']
    j = int()

    for i in range(num):
        if(art[i]['title'] and art[i]['url']):
            titles.append(art[i]['title'])
            urls.append(art[i]['url'])
            descriptions.append(art[i]['description'])
            sources.append(art[i]['source']['name'])
            image_urls.append(art[i]['urlToImage'])
            for char in chars:
                art[i]['publishedAt'] = art[i]['publishedAt'].replace(char,' ')
            dateTime.append(art[i]['publishedAt'])
    
    return render_template("topnews.html", **locals())

def req_news_search(search_input):
    today = date.today()
    date_today = today.strftime("%Y-%m-%d")
    url = ('http://newsapi.org/v2/everything?'
        'q='+search_input+'&'
        'from='+date_today+'&'
        'sortBy=popularity&'
        'apiKey=8ecd5ce9df6c478a8ccae9b4a4817cf6')
        
    response = requests.get(url)
    res = response.json()
    art = res['articles']
    num = len(art)
    titles = []
    urls = []
    descriptions = []
    sources = []
    dateTime = []
    image_urls = []
    chars = ['T','Z']
    j = int()

    for i in range(num):
        if(art[i]['title'] and art[i]['url']):
            titles.append(art[i]['title'])
            urls.append(art[i]['url'])
            descriptions.append(art[i]['description'])
            sources.append(art[i]['source']['name'])
            image_urls.append(art[i]['urlToImage'])
            for char in chars:
                art[i]['publishedAt'] = art[i]['publishedAt'].replace(char,' ')
            dateTime.append(art[i]['publishedAt'])
    
    return render_template("topnews.html", **locals())