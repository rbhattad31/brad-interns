import requests

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.content)

print(x.text)
print('=' * 20)
r = requests.post('https://w3schools.com/python/demopage.htm', data={'key': 'value'})

print(r)
print('=' * 20)
r = requests.delete('https://w3schools.com/python/demopage.htm', data={'key': 'value'})

print(r)
print("=" * 20)
r = requests.head('https://httpbin.org/', data={'key': 'value'})

print(r)

print(r.headers)

print("=" * 20)
