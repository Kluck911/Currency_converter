import redis


red = redis.Redis(
    host='redis-17900.c250.eu-central-1-1.ec2.cloud.redislabs.com',
    port=17900,
    password='yMmNPTv7twPJtD1nRvAGAaaBzkTUvOHm'
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('Name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('Name:\t')
        phone = red.delete(name)
        if phone:
            print(f'{name}\'s phone has been deleted')
        else:
            print(f'Not found {name}')
    elif action == 'stop':
        break
