import requests
import json

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json = json.dumps(data))

print(r.content)