import requests
import json


r = requests.get('https://api.github.com')
d = json.loads(r.content)

print(type(d))
print(d['following_url'])

for key, v in d.items():
    print('{0}: {1}'.format(key, v))
