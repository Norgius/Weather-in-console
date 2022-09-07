import requests

cities = ('Лондон', 'Шереметьево', 'Череповец')
url_template = 'https://wttr.in/{}'
params_request = {'MnTq': '', 'lang': 'ru'}

for city in cities:
    response = requests.get(url_template.format(city), params=params_request)
    response.raise_for_status()
    print(response.text)
