from django.shortcuts import render

# This is my views in djnago

def home(request):
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=~distance~&API_KEY=9034563F-7773-4C12-92E0-E1DDD216565A
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=9034563F-7773-4C12-92E0-E1DDD216565A");

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api' : api})
 

def about(request):
    return render(request, 'about.html', {})