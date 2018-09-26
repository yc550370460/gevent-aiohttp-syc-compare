from gevent import monkey; monkey.patch_all()
import gevent
import requests
import time

url_list = ["https://www.python.org/", "https://www.yahoo.com/", "https://www.github.com/", "https://www.baidu.com/",
            "http://pts2.stm.com/", "https://www.python.org/",
            "https://bbs.hupu.com/23714651-2.html","https://bbs.hupu.com/23714651-1.html",
            "https://bbs.hupu.com/23714651-3.html", "https://bbs.hupu.com/23714651-4.html",
            "https://bbs.hupu.com/23714651-5.html", "https://bbs.hupu.com/23714651-6.html",
            "https://bbs.hupu.com/23714651-7.html","https://bbs.hupu.com/23714651-8.html",
            "https://bbs.hupu.com/23714651-9.html", "https://bbs.hupu.com/23714651-10.html", "https://www.google.com/",
            "https://www.z.cn/", "https://www.jd.com/"]
count = 1
# gevent count = len(url_list) / count

tmp_start = time.time()
print tmp_start


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url, verify=False)
    print resp.text
    print('%d bytes received from %s.' % (len(resp.text), url))


def f_list(list):
    for item in list:
        f(item)

for i in range(count):
    jobs = list()
    left = i * (len(url_list) // count)
    if (i + 1) * (len(url_list) // count) < len(url_list):
        right = (i + 1) * (len(url_list) // count)
    else:
        right = len(url_list)
    for item in url_list[left: right]:
        jobs.append(gevent.spawn(f, item))
    gevent.joinall(jobs)



# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'https://www.github.com/'),
#         gevent.spawn(f, 'https://www.baidu.com/'),
#         gevent.spawn(f, 'http://pts2.stm.com/'),
# ])
end_time = time.time()
print end_time
print end_time - tmp_start
