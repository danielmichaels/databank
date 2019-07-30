import requests
import json
import base64

b64 = base64.b64decode(requests.post(
   "https://www.hackthebox.eu/api/invite/generate", json={'key':'value'}).json()['data']['code'])

print('[*] HackTheBox invite code...')
print('[*] connecting to servers...')
print('[!] Code found: {}'.format(b64))

