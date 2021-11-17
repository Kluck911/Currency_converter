import redis

red = redis.Redis(
    host='redis-17900.c250.eu-central-1-1.ec2.cloud.redislabs.com',
    port=17900,
    password='yMmNPTv7twPJtD1nRvAGAaaBzkTUvOHm'
)


red.set('var1', 'value1') # записываем в кеш строку "value1"

print(red.get('var1')) # считываем из кэша данные