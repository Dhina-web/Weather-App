from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import requests #pip install requets then import it to django
from .models import City
from .forms import CityForm
from django.contrib import messages
# Create your views here.
def weather(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=79a87d3bd7e00e903faa18fe14a0fb17'
	meassage =''
# this if fucntion is for displaying the weather for city from our database
	if request.method == 'POST':
		form = CityForm(request.POST)
#this if is for if a city already exisits it prevent it from adding again
		if form.is_valid():
			new_city = form.cleaned_data['name']
			existing_city_count = City.objects.filter(name=new_city).count()#flitering the city name from City class
#and putting them as a count value if a count is 0 means city doesn't exisit
			if existing_city_count == 0:
				r= requests.get(url.format(new_city)).json()# R is going to return the data for the city that gets added
			#cod means a code word to find if the city is exist or not if cod is 200 then the city is exists in world
				if r['cod'] ==200:
					form.save()
				else:
					meassage ='City Doesnot exists'
			else:
				meassage = 'City is already exists'

	form = CityForm()

	citys = City.objects.all() # to dispaly all the cites in our database

	weather_data = [] #to get the weather to each city and appened it to the list 
# these are all for API communications
	for city in citys:

		r= requests.get(url.format(city)).json() # this for getting the openweathermap data by making requests

		broadcast ={ # this is a python dictionary there are the fields that we want to display from the api json details
			'city' : city.name,
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
		}

		weather_data.append(broadcast) 
		''' 
		for loop is going to loop over through all the cites we have in our
		database for each city it's going to query the APi the queired data will be send to broadcast dictionary
		and that broadcast data is going to append on to the weather data list 
		'''

	print(weather_data)
	context = {'weather_data': weather_data, 'form': form, 'meassage':meassage}
	return render(request,'index.html', context)

def del_city(request, city_name):
	City.objects.get(name=city_name).delete()
	return redirect('index')