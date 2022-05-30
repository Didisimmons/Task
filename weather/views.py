import requests, datetime
from django.shortcuts import render,  get_object_or_404
from .forms import SensorForm
from .models import Sensor

# Create your views here.

def index(request):
    if request.method == 'POST':
       form = SensorForm(request.POST)
       form.save()

    form = SensorForm()

    sensors = Sensor.objects.all()

    weather_data = []

    for w_data in sensors:
        url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid="
        country = w_data.country
        city = w_data.city_name
        id = w_data.sensor_id
        r = requests.get(url.format(city,country)).json()
        #request the API data and convert the JSON to Python data types
        sensor_weather = {
            'id': w_data.sensor_id,
            'city' : w_data.city_name,
            'country' : w_data.country,
            'temperature' : r["main"]["temp"],
            'humidity' : r['main']['humidity'],
            'pressure' : r['main']['pressure'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],    
            'wind_speed' : r['wind']['speed'], 
            'long' : r['coord']['lon'],
            'lat' : r['coord']['lat'],
        }
        print(sensor_weather)
        weather_data.append(sensor_weather)
    day = datetime.date.today()
    template = 'weather/index.html'
    context = {
        'form' : form,
        'weather_data': weather_data,
        'day': day
    }
    return render(request, template, context)


def result(request, sensor_id):
    sensors = get_object_or_404(Sensor, pk=sensor_id)
    country = sensors.country
    city = sensors.city_name
    print(country)
    print(city)

    url = "http://api.openweathermap.org/data/2.5/forecast?q={},{}&appid="
   
    r = requests.get(url.format(city, country)).json()
    
    #request the API data and convert the JSON to Python data types
    single_weather = {
        'temperature' : r["list"][0]["main"]["temp"],
        'city' : city,
        'country' : country,
    }
    

    template = 'weather/single_view.html'
    context = {
        'sensors': sensors,
        'single_weather' :single_weather,

    }
    return render(request, template, context)