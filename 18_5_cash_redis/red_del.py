import redis


red = redis.Redis(
    host='redis-17900.c250.eu-central-1-1.ec2.cloud.redislabs.com',
    port=17900,
    password='yMmNPTv7twPJtD1nRvAGAaaBzkTUvOHm'
)

red.delete('dict1')

print(red.get('dict1'))
