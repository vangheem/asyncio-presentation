import asyncio
import aiohttp


async def download_url(url):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        text = await resp.text()
        print(f'Downloaded {url}, size {len(text)}')


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(
    download_url('https://www.google.com'),
    download_url('https://www.facebook.com'),
    download_url('https://www.twitter.com'),
    download_url('https://www.stackoverflow.com')
))
