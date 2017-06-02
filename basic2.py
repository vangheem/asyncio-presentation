import asyncio


async def hello1():
    await asyncio.sleep(0.5)
    print('hi 1')


async def hello2():
    print('hi 2')


event_loop = asyncio.get_event_loop()
future1 = asyncio.ensure_future(hello1(), loop=event_loop)
future2 = asyncio.ensure_future(hello2(), loop=event_loop)
event_loop.run_until_complete(future2)
event_loop.run_until_complete(future1)
