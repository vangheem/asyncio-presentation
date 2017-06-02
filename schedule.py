import asyncio


def delayed_print(txt):
    print(txt)


event_loop = asyncio.get_event_loop()
event_loop.call_later(1, delayed_print, 'Hello')
event_loop.call_at(event_loop.time() + 1, delayed_print, 'Hello timed')
event_loop.run_until_complete(asyncio.sleep(2))
