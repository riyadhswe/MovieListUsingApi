from django.shortcuts import render
import requests
import json


# Create your views here.

def index(request):
    api_request = requests.get("https://drfmovie.herokuapp.com/movie/?format=json")
    try:
        api = json.loads(api_request.content)
    except:
        api = "Error"
    return render(request, 'index.html', {'api': api})
