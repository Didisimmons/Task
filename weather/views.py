import requests, datetime, math
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
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
        url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}"
        api_key = settings.API_KEY
        country = w_data.country
        city = w_data.city_name
        id = w_data.sensor_id
        r = requests.get(url.format(city, country, api_key)).json()
        #request the API data and convert the JSON to Python data types
        sensor_weather = {
            'id': w_data.sensor_id,
            'city' : w_data.city_name,
            'country' : w_data.country,
            'temperature' : r["main"]["temp"],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],    
        }
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
    id = sensors.sensor_id,
    api_key = settings.API_KEY

    url = "http://api.openweathermap.org/data/2.5/forecast?q={},{}&appid={}"
   
    r = requests.get(url.format(city, country, api_key)).json()
    
    #request the API data and convert the JSON to Python data types
    single_weather = {
        'id' : id,
        'city' : city,
        'country' : country,
        "pressure":r["list"][0]["main"]["pressure"],
        "wind": r['list'][0]['wind']['speed'],
        "degree": r['list'][0]['wind']['deg'],
        "humidity": r["list"][0]["main"]["humidity"],
        "description": r['list'][0]['weather'][0]['description'],
        "temperature": round(r["list"][0]["main"]["temp"] - 273.0),
        "temp_min1": math.floor(r["list"][1]["main"]["temp_min"] - 273.0),
        "temp_max1": math.ceil(r["list"][1]["main"]["temp_max"] - 273.0),
        "temp_min2": math.floor(r["list"][2]["main"]["temp_min"] - 273.0),
        "temp_max2": math.ceil(r["list"][2]["main"]["temp_max"] - 273.0),
        "temp_min3": math.floor(r["list"][3]["main"]["temp_min"] - 273.0),
        "temp_max3": math.ceil(r["list"][3]["main"]["temp_max"] - 273.0),
        "temp_min4": math.floor(r["list"][4]["main"]["temp_min"] - 273.0),
        "temp_max4": math.ceil(r["list"][4]["main"]["temp_max"] - 273.0),
        "temp_min5": math.floor(r["list"][5]["main"]["temp_min"] - 273.0),
        "temp_max5": math.ceil(r["list"][5]["main"]["temp_max"] - 273.0),
        "temp_min6": math.floor(r["list"][6]["main"]["temp_min"] - 273.0),
        "temp_max6": math.ceil(r["list"][6]["main"]["temp_max"] - 273.0),
        
        'date': r['list'][0]["dt_txt"],
        'date1': r['list'][1]["dt_txt"],
        'date2': r['list'][2]["dt_txt"],
        'date3': r['list'][3]["dt_txt"],
        'date4': r['list'][4]["dt_txt"],
        'date5': r['list'][5]["dt_txt"],
        'date6': r['list'][6]["dt_txt"],
        
        "icon": r["list"][0]["weather"][0]["icon"],
        "icon1": r["list"][1]["weather"][0]["icon"],
        "icon2": r["list"][2]["weather"][0]["icon"],
        "icon3": r["list"][3]["weather"][0]["icon"],
        "icon4": r["list"][4]["weather"][0]["icon"],
        "icon5": r["list"][5]["weather"][0]["icon"],
        "icon6": r["list"][6]["weather"][0]["icon"],
    }
    
    template = 'weather/single_view.html'
    context = {
        'sensors': sensors,
        'single_weather' :single_weather,
    }
    return render(request, template, context)


def delete_sensor(request, sensor_id):
    sensors = get_object_or_404(Sensor, pk=sensor_id)
    sensors.delete()
    return redirect(reverse('home'))
