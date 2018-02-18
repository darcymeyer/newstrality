import json
import requests

username= "b5a2fef5-4737-4e0d-b8eb-fc74816af24d"
password= "23YY3My8YbYN"

def get_entities_and_concepts(text):
    params = {
        ('version', '2017-02-27'),
        ('text', text),
        ('features', 'sentiment,entities,concepts'),
        ('keywords.sentiment', 'true'),
    }
    auth = (username, password)
    r = requests.get("https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze", params=params, auth=auth)
    t = json.loads(r.text)
    concepts = sorted(t['concepts'], key=lambda x: x['relevance'], reverse=True)
    entities = sorted(t['entities'], key=lambda x: x['relevance'], reverse=True)
    entities = [e['text'] for e in entities]
    concepts = [c['text'] for c in concepts]
    return entities[:min(5, len(entities))], concepts[:min(5, len(concepts))]
