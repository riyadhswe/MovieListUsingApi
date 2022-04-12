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


def action(request):
    api_request = requests.get("https://drfmovie.herokuapp.com/action/?format=json")
    try:
        api = json.loads(api_request.content)
    except:
        api = "Error"
    return render(request, 'action.html', {'api': api})


def comedy(request):
    api_request = requests.get("https://drfmovie.herokuapp.com/comedy/?format=json")
    try:
        api = json.loads(api_request.content)
    except:
        api = "Error"
    return render(request, 'comedy.html', {'api': api})
