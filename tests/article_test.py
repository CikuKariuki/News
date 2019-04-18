import unittest
from models import article

Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the articles class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_article = Article("bbc-news","BBC NEWS","BBC News","Italian students fined €13m over BBQ forest fire","The two 22-year old men are fined the sum after a meal at a mountain forest home goes badly wrong","http://www.bbc.co.uk/news/world-europe-47960358","https://ichef.bbci.co.uk/news/1024/branded_news/436A/production/_106485271_gettyimages-1039913538.jpg","2019-04-17T10:09:34Z","Image copyrightGetty ImagesImage caption\r\n Italian firefighters battled the large blaze for days in December and January (file photo)\r\nTwo university students blamed for a forest fire in the Italian region of Como have been fined 13.5m (£11.7m).\r\nThe men, bot… [+2068 chars]")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()