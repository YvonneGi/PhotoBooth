from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from display import urls
from .models import Images,Category,Location


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def display_image(request):
    date = dt.date.today()
    return render(request, 'today.html', {"date": date})