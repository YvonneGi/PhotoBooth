from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from display import urls
from .models import Images,Category,Location


# Create your views here.
def welcome(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'welcome.html',{'locations':locations,'categories':categories})

def display_image(request):
    date = dt.date.today()
    return render(request, 'all-photos/today.html', {"date": date})

# def single_photo(request, photo_id):
#     images = Images.objects.get(id=photo_id)
#     return render(request, 'all-photos/single_image.html', {'images': images})

def all_images(request):
    images = Images.get_images()
    return render(request, 'all-photos/all_images.html', {"images": images})

def search_images(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_photo = Images.search_by_cat_name(search_term)
        message = f"{search_term}"
        return render(request, 'all-photos/search_image.html', {"message": message, "images": searched_photo})
    else:
        message = 'You haven\'t searched for any photos.'
        return render(request, 'all-photos/search_image.html', {"message": message})

# def page_category(request,category):
#     locations = Location.objects.all()
#     categories = Category.objects.all()
#     category_results = Images.search_category(category)
#     return render(request,'welcome.html',{'locations':locations,'categories':categories})

# def page_location(request,location):
#     locations = Location.objects.all()
#     categories = Category.objects.all()
#     location_results = Image.filter_location(location)
#     return render(request,'welcome.html',{'locations':locations,'categories':categories})
