from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(sources):
    '''
    gets json response to url request
    '''
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read() #to read response
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list) #takes in a list of dictionary objects and returns a list of news objects
    
    return news_results #list of news objects

def process_results(news_list):
    '''
    function that processes the news result and transforms them to a list of Objects
    
    Args: news_list: dictionaries that contain news details
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        language = news_item.get('language')

        if language == "en":
            news_object = News(id,name,description,language)
            news_results.append(news_object)

    return news_results

