from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from . import map
import folium
import geopy
import requests
import urllib.parse
from geopy.geocoders import Nominatim
# view in the client side
# Create your views here.

def home(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        location = request.POST.get('location')

        print(price, '  ', location)
    # address = 'באר שבע, שכונה ד'
    # url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
    #
    # response = requests.get(url).json()
    # print(response[0]["lat"])
    # print(response[0]["lon"])



    return render(request, 'index.html')


# The Implementation Is Just for FUN!
def SearchResultsView(request):
    # if request.method == 'POST':
    #     item = request.POST.get('search')
    #     location = request.POST.get('location')
    #     print(item, '  ', location)

    return HttpResponse("request")


class FoliumView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        m = folium.Map(
            location=[45.372, -121.6972],
            zoom_start=12,
            tiles='Stamen Terrain'
        )
        m.add_to(figure)

        folium.Marker(
            location=[45.3288, -121.6625],
            popup='Mt. Hood Meadows',
            icon=folium.Icon(icon='cloud')
        ).add_to(m)

        folium.Marker(
            location=[45.3311, -121.7113],
            popup='Timberline Lodge',
            icon=folium.Icon(color='green')
        ).add_to(m)

        folium.Marker(
            location=[45.3300, -121.6823],
            popup='Some Other Location',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        figure.render()
        return {"map": figure}




def show_items(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        location = request.POST.get('location')

        print(price, '  ', location)
    list = ['Bern', 'Bob', 'Epifanio', 'El pug']
    return render(request, "items_list.html", {"list": list})

def show_results(request):
    if request.method == 'POST':
        item = request.POST.get('options')
        print(item)
    # creation of map comes here + business logic
    m = folium.Map([51.5, -0.25], zoom_start=10)
    test = folium.Html('<b>Hello world</b>', script=True)
    popup = folium.Popup(test, max_width=650)
    folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    m = m._repr_html_()  # updated
    list = ['Bern', 'Bob', 'Epifanio', 'El pug']
    context = {'my_map': m,"list": list}
    return render(request, 'map.html', context)