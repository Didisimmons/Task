import requests, datetime
from django.shortcuts import render , get_list_or_404
from .forms import SensorForm
from .models import Sensor

# Create your views here.

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid=api_key"

    if request.method == 'POST':
        pass

    form = SensorForm()

    sensors = Sensor.objects.all()

    weather_data = []

    for w_data in sensors: 
        country = w_data.city_name
        city = w_data.country
        r = requests.get(url.format(city,country)).json()
        #request the API data and convert the JSON to Python data types
        sensor_weather = {
            'city' : w_data.city_name,
            'country' :  w_data.country,
            'temperature' : r['main']['temp'],
            'humidity' : r['main']['humidity'],
            'pressure' : r['main']['pressure'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],    
            'wind_speed' : r['wind']['speed'], 
        }
        print(sensor_weather)
        weather_data.append(sensor_weather)
        print(weather_data)

    day = datetime.date.today()

    template = 'weather/index.html'
    context = {
        'form' : form,
        'weather_data': weather_data,
        'day': day
    }
    return render(request, template, context)


