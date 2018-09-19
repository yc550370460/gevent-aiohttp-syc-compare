import aiohttp
import time
import asyncio

tmp_start = time.time()
print(tmp_start)

url_list = ['https://www.python.org/', 'https://www.yahoo.com/', 'https://www.github.com/', 'https://www.baidu.com/',
            'http://pts2.stm.com/']

# env: python3.6 above and aiohttp is required
async def f():
    async with aiohttp.ClientSession(connector_owner=True) as session:
        for index, url in enumerate(url_list):
            print('GET: %s' % url)
            async with session.get(url, verify_ssl=False) as res:
                print('%d bytes received from %s.' % (len(str(res)), url))

loop = asyncio.get_event_loop()
tasks = f()
loop.run_until_complete(tasks)
loop.close()
end_time = time.time()
print(end_time)
print(end_time - tmp_start)