import asyncio
import requests
import concurrent.futures


def download_url(url):
    resp = requests.get(url)
    text = resp.content
    print(f'Downloaded {url}, size {len(text)}')


async def foobar():
    print('foobar')


executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(
    event_loop.run_in_executor(executor, download_url, 'https://www.google.com'),
    event_loop.run_in_executor(executor, download_url, 'https://www.facebook.com'),
    event_loop.run_in_executor(executor, download_url, 'https://www.twitter.com'),
    event_loop.run_in_executor(executor, download_url, 'https://www.stackoverflow.com'),
    foobar()
))
