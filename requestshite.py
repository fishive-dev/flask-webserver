import requests
from flask import jsonify
payload = {
    'uno' : "Hi",
    'dos' : "Hello there"
}

#get = requests.get('http://192.168.2.217:42069/processGet')
post = requests.post('http://192.168.2.217:42069/processPost', payload)
print(post.text)
