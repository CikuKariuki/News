from flask import render_template
from app import app
from .request import get_news, get_article

# Views
@app.route('/')
def index():

    '''
    function that returns the index page and its data
    '''
    #getting news sources
    news_sources = get_news()
    # print(news_sources)
    title = 'Home -News Highlights from all over the world'
    return render_template('index.html', title = title, sources = news_sources)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    returns the news details page and its data
    '''
    return render_template('news.html', id=news_id)

@app.route('/article/<article_id>')
def article(article_id):
    '''
    returns the articles page and its data
    '''
    return render_template('article.html', id = article_id)