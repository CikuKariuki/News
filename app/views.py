from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    function that returns the index page and its data
    '''
    message = "News Highlights"
    return render_template('index.html', message = message)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    returns the news details page and its data
    '''
    return render_template('news.html', id=news_id)