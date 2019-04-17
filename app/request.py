from app import app
import urllib.request,json
from .models import news,article

News = news.Sources
Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url = app.config["ARTICLE_API_BASE_URL"]


def get_news(): 
    '''
    gets json response to url request
    '''
    get_news_url = base_url.format(api_key) #.format and base_url pass in the news source and api-key
    with urllib.request.urlopen(get_news_url) as url: #with is used here as a context manager that takes in get_news_url as an argument and sends a request as url
        get_news_data = url.read() #to read response
        get_news_response = json.loads(get_news_data) #to convert json response to a python dictionary

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_results(news_sources_list) #takes in a list of dictionary objects and returns a list of news objects
    
    return news_sources #list of news objects

def process_results(news_sources_list):
    '''
    function that processes the news result and transforms them to a list of Objects
    
    Args: news_list: dictionaries that contain news details
    '''
    news_sources = [] #empty list to store newly created news objects
    for news_item in news_sources_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')

        if language == "en":
            news_object = News(id,name,description,url,category,language)
            news_sources.append(news_object)

    return news_sources

def get_article(id):
        '''
        function that gets the json response to our url request
        '''
        get_article_url = article_base_url.format(id,api_key)

        with urllib.request.urlopen(get_article_url) as url:
                get_article_data = url.read()
                get_article_response = json.loads(get_article_data)

                news_article = None

                if get_article_response['article']:
                        news_article_list =get_news_response['article']
                        news_article = process_article(news_article_list)

        return news_article

def process_article(article_list):
        '''
        function that processes the article results and transforms them to a list of objects
        '''
        news_article = []
        for article in article_list:
                id = article['source']['id']
                name = article.get('name')
                author = article.get('author')
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')
                urlToImage = article.get('urlToImage')
                publishedAt = article.get('publishedAt')
                content = article.get('content')
 
                article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt,content)
                news_article.append(article_object)

        return news_article