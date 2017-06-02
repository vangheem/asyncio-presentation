import asyncio


async def yelleding():
    result = []
    for idx in range(5):
        print(f'Before yelleding {idx}')
        result.append(idx)
    return result


async def foobar2():
    for idx in await yelleding():
        print(f"Yay, I've been yelleded {idx}")


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(foobar2())
