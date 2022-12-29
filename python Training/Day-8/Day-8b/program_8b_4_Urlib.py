import urllib.request

x = urllib.request.urlopen('https://www.google.com/')
print(x.read())
url = 'https://www.google.com/search'
values = {'q': 'python programming tutorials'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')  # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
