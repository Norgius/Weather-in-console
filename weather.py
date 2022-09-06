import requests

cities = ('Лондон', 'Шереметьево', 'Череповец')
url_template = 'https://wttr.in/{}?nTqM&lang=ru'

for city in cities:
    response = requests.get(url_template.format(city))
    response.raise_for_status()
    print(response.text)
