import tornado.ioloop
import tornado.web
import json
from newspaper import Article
import urllib
from watson_api import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #tmp = {"analysis": [0, 1, .2, .4], "ideologies": [-1, 1, .1, -.4], "topic": ["topic_1", "topic_2", "topic_3", "topic_4"], "entities": ["entity_1", "entity_2", "entity_3", "entity_4"]}
        tmp = [{"analysis":0,
            "ideology":-1,
            "topics":["one", "two"],
            "entities":["one", "two"]},
           {"analysis":0.2,
            "ideology":0.5,
            "topics":["three", "four"],
            "entities":["cat", "dog"]}
           ]
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(json.dumps(tmp))

    def post(self):
        data = self.get_argument('url')
        data = urllib.parse.unquote(data)
        article = Article(data)
        article.download()
        article.parse()
        text = article.text
        words = len(text.split(" "))/len(text.split("\n"))
        e, c = get_entities_and_concepts(text)
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        json_response = json.dumps({'ideology':0, 'analysis':words, 'entities':e, 'topics':c})
        self.write(json_response)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
