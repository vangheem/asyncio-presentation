import asyncio


async def hello():
    print('hi')


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(hello())
