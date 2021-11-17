import redis
import json


red = redis.Redis(
    host='redis-17900.c250.eu-central-1-1.ec2.cloud.redislabs.com',
    port=17900,
    password='yMmNPTv7twPJtD1nRvAGAaaBzkTUvOHm'
)


dict1 = {'key1': 'value1', 'key2': 'value2'}
red.set('dict1', json.dumps(dict1))
converted_dict = json.loads(red.get('dict1'))

print(type(converted_dict))
print(converted_dict)
