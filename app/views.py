from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    function that returns the index page and its data
    '''
    title = 'Home -News Highlights from all over the world'
    return render_template('index.html', title = title)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    returns the news details page and its data
    '''
    return render_template('news.html', id=news_id)