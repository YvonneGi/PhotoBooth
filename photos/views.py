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

def single_photo(request, photo_id):
    photo = Images.objects.get(id=photo_id)
    return render(request, 'single_image.html', {'photo': photo})

def all_images(request):
    images = Images.get_images()
    return render(request, 'all_images.html', {"images": images})

def search_images(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photo = Images.search_by_cat_name(search_term)
        photos = Images.objects.filter(name=searched_photo).all()
        message = f"{search_term}"
        return render(request, 'search_image.html', {"message": message, "photos": searched_photo})
    else:
        message = 'You haven\'t searched for any photos.'
        return render(request, 'search_image.html', {"message": message})
