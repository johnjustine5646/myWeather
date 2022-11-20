from django.shortcuts import render

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f0d345e3321ea2ada0be02c622db15b0'

    city1="Kottayam"
    city1 = requests.get(url.format(city1)).json() #we are requesting the API data and converting the JSON to Python data types
    weather1 = {
        'city' : city1['name'],
        'temperature' : city1['main']['temp'],
        'description' : city1['weather'][0]['description'],
        'wind' : city1['wind']['speed'],
        'icon' : city1['weather'][0]['icon'],
        'country' : city1['sys']['country']
    }

    city2 = 'Pune'
    city2 = requests.get(url.format(city2)).json() #we are requesting the API data and converting the JSON to Python data types
    weather2 = {
        'city' : city2['name'],
        'temperature' : city2['main']['temp'],
        'description' : city2['weather'][0]['description'],
        'wind' : city2['wind']['speed'],
        'icon' : city2['weather'][0]['icon'],
        'country' : city2['sys']['country']
    }


    return render(request, 'index.html', {'weather1' : weather1,'weather2':weather2}) #returns the index.html template

    