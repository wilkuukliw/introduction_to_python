# req.py

import requests

req = requests.get('https://pypi.org/')

print(req.text)

