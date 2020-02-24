# req.py


import requests

r = requests.get('https://api.github.com/users/victorexposito/repos')

print(r.text)
