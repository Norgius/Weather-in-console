import requests

cities = ('Лондон', 'Шереметьево', 'Череповец')
url_template = 'https://wttr.in/{}'
request_params = {'MnTq': '', 'lang': 'ru'}

for city in cities:
    response = requests.get(url_template.format(city), params=request_params)
    response.raise_for_status()
    print(response.text)
