import asyncio


async def print_foobar1():
    print('foobar1')


async def print_foobar2():
    print('foobar2')


async def foobar():
    await print_foobar1()
    print_foobar2()  # won't work, never awaited


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(foobar())
print_foobar1()  # won't work, never awaited
# await print_foobar1()  # error, not running in event loop
