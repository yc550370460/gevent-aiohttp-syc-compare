import requests
import time

tmp_start = time.time()
print tmp_start
def f(url):
    print('GET: %s' % url)
    resp = requests.get(url, verify=False)
    print resp.text
    print('%d bytes received from %s.' % (len(resp.text), url))

url_list = ['https://www.python.org/', 'https://www.yahoo.com/', 'https://www.github.com/', 'https://www.baidu.com/', 'http://pts2.stm.com/']
for item in url_list:
    f(item)

end_time = time.time()
print end_time
print end_time - tmp_start