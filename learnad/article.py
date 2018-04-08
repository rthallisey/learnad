import sys
import os
from newspaper import Article

PROJECT_ROOT = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__))))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

class News(object):

    def __init__(self, url):
        self.url = url
        self.article = Article(url)
        self.article.download()
        self.article.parse()
        self.text = self.article.text
        self.authors = self.article.authors
        self.title = self.article.title
        self.keywords = self.article.keywords
        self.summary = self.article.summary
