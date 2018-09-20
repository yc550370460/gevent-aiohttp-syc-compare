import aiohttp
import time
import asyncio



url_list = ['https://www.python.org/', 'https://www.yahoo.com/', 'https://www.github.com/', 'https://www.baidu.com/',
            'http://pts2.stm.com/']

# env: python3.6 above and aiohttp is required
async def fetch(session, url):
    print('GET: %s' % url)
    async with session.get(url, verify_ssl=False) as res:
        res = await res.text()
        print(res)
        print('%d bytes received from %s.' % (len(str(res)), url))

async def main():
    async with aiohttp.ClientSession(connector_owner=True) as session:
        for url in url_list:
            await fetch(session, url)




async def handle_tasks(task_id, work_queue):
    async with aiohttp.ClientSession(connector_owner=True) as session:
        while not work_queue.empty():
            current_url = await work_queue.get()
            try:
                await fetch(session, current_url)
            except Exception as e:
                print(e)
                print("error")


def eventloop():
    q = asyncio.Queue()
    [q.put_nowait(url) for url in url_list]
    loop = asyncio.get_event_loop()
    tasks = [handle_tasks(task_id, q, ) for task_id in range(5)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    tmp_start = time.time()
    print(tmp_start)

    eventloop()

    end_time = time.time()
    print(end_time)
    print(end_time - tmp_start)
