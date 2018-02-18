import json
import requests

username= "b5a2fef5-4737-4e0d-b8eb-fc74816af24d"
password= "23YY3My8YbYN"

def get_entities(text):
    params = {
        ('version', '2017-02-27'),
        ('text', text),
        ('features', 'sentiment,keywords'),
        ('keywords.sentiment', 'true'),
    }
    auth = (username, password)
    r = requests.get("https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze", params=params, auth=auth)
    t = json.loads(r.text)
    entities = sorted(t['keywords'], key=lambda x: x['relevance'], reverse=True)
    return entities[:max(5, len(entities))]
