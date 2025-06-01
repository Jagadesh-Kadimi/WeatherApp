from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
def home(request):
    if 'city' in request.POST:
         city=request.POST['city']
    else:
        city='eluru'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=df642833e9741bf47ea80e4466688b6a'
    PARAMS = {
                'units':'metric'
            }
    API_KEY='AIzaSyDiaPnRTWsbzPsqE0AhebrWvO7FaT3-rf8'
    SEARCH_ENGINE_ID = '0746cfadbe91c4a3f'
    query = f"popular places in {city}"
    page = 1
    start = (page - 1) * 10 + 1
    searchtype = 'image'
    search_url = (
        f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}'
        f'&q={query}&searchType={searchtype}&start={start}&imgSize=large'
    )
    search_data = requests.get(search_url).json()
    search_item = search_data.get("items")
    if search_item and len(search_item) > 0:
        image_url = search_item[0]['link']
    else:
        image_url = None
    
    data=requests.get(url,PARAMS).json()
    if 'weather' in data and data['weather']:
        description = data['weather'][0].get('description', 'No description')
        icon = data['weather'][0].get('icon', '')
    else:
        description = 'No weather data'
        icon = ''
    visibility = data.get('visibility', 'N/A')
    cloud = data.get('clouds', {}).get('all', 'N/A')
    icon = data['weather'][0]['icon'] if 'weather' in data and data['weather'] else ''
    temp = data['main']['temp'] if 'main' in data and 'temp' in data['main'] else 'N/A'
    humidity = data['main']['humidity'] if 'main' in data and 'humidity' in data['main'] else 'N/A'
    wind=data['wind']['speed'] if 'wind' in data and 'speed' in data['wind']else 'N/A'
    country=data['sys']['country'] if 'sys' in data and 'country' in data['sys'] else 'N/A'
    city=data['name'] if 'name' in data else 'N/A'
    date = datetime.datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
    sunrise = 'N/A'
    sunset = 'N/A'
    if 'sys' in data and 'sunrise' in data['sys'] and 'sunset' in data['sys']:
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M:%S %p')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M:%S %p')
        date = datetime.datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
    pressure=data['main']['pressure'] if 'main' in data and 'pressure' in data['main'] else 'N/A'
    context={
        'city':city,
        'country':country,
        'description':description,
        'icon':icon,
        'temp':temp,
        'humidity':humidity,
        'wind':wind,
        'date':date,
        'visibility':visibility,
        'cloud':cloud,
        'sunrise':sunrise,
        'sunset':sunset,
        'pressure':pressure,
        'image_url':image_url
    }
    return render(request,'index.html',context)

 