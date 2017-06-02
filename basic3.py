import asyncio
import random


async def hello_many():
    while True:
        number = random.randint(0, 3)
        await asyncio.sleep(number)
        print('Hello {}'.format(number))


event_loop = asyncio.get_event_loop()
task = asyncio.Task(hello_many())
print('task running now...')
event_loop.run_until_complete(asyncio.sleep(10))
print('we waited 10 seconds')
task.cancel()
print('task cancelled')
