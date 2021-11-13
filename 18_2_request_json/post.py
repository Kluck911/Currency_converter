import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json = json.dumps(data))
texts = json.loads(r.content)

print(r.content)