# req.py

import requests


req = requests.get('https://pypi.org/')

print(req.text)            # downloading page's text // can cave later to index.

