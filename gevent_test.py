from gevent import monkey; monkey.patch_all()
import gevent
import requests
import time

tmp_start = time.time()
print tmp_start
def f(url):

    print('GET: %s' % url)
    resp = requests.get(url, verify=False)
    print resp.text
    print('%d bytes received from %s.' % (len(resp.text), url))


gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.github.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'http://pts2.stm.com/'),
])
end_time = time.time()
print end_time
print end_time - tmp_start
