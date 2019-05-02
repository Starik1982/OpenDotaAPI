import urllib.request
import requests
import json
from django.shortcuts import render, render_to_response, redirect


# Create your views here.


def main(request):
    args = {}
    return render_to_response('main.html', args)


def get_update(self):
    url = 'https://api.opendota.com/api/publicMatches'
    r = requests.get(url)
    data = r.json()
    print(data)
    return render_to_response('main.html', data[0])
