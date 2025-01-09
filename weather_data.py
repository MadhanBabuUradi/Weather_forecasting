import requests

city_name = 'Hyderabad'
API_Key = 'c23c29d2bd43cba3cb3db62298c64b65'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},&appid={API_Key}&units=metric'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data['weather'][0]['description'])
    print('Current temperature is:', data['main']['temp'])