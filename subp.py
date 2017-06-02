import asyncio


async def run_cmd(cmd):
    print(f'Executing: {" ".join(cmd)}')
    process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)
    out, error = await process.communicate()
    print(out.decode('utf8'))


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(
    run_cmd(['sleep', '1']),
    run_cmd(['echo', 'hello'])
))
