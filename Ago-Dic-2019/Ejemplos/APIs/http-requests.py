import requests

# https://requests.readthedocs.io/en/master/
# https://github.com/psf/requests/

r = requests.get('https://jsonplaceholder.typicode.com/users')

print(r)
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.text)
print(r.json())