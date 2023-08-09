import requests
import random
from datetime import datetime, timedelta
from django.shortcuts import render

def random_apod(request):
    apod_url = "https://api.nasa.gov/planetary/apod"
    api_key = "8iIWzRYktgxJepmh8m2aurDh4ZvjrmVsLtuSg0kT"

    start_date = datetime(2000, 1, 1)
    end_date = datetime.today()
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    params = {
        "api_key": api_key,
        "hd": True,
        "date": random_date.strftime("%Y-%m-%d")
    }

    response = requests.get(apod_url, params=params)
    data = response.json()

    image_url = data.get("hdurl")
    image_date = random_date.strftime('%Y-%m-%d')

    context = {
        "image_url": image_url,
        "image_date": image_date,
    }

    return render(request, "space1/random_apod.html", context)
