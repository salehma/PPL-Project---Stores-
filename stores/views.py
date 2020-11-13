from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView, ListView


# view in the client side
# Create your views here.

def home(request):
    print(request)
    if request.method == 'POST':
        item = request.POST.get('search')
        location = request.POST.get('location')
        print(item, '  ', location)
    return render(request, 'index.html')


# The Implementation Is Just for FUN!
def SearchResultsView(request):
    if request.method == 'POST':
        item = request.POST.get('search')
        location = request.POST.get('location')
        print(item, '  ', location)
    return render(request, 'as.html')
