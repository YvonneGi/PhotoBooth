from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$', views.display_image, name='Today'),
    # url(r'^photo/(\d+)', views.single_photo, name='singlePhoto'),
    url(r'^search/', views.search_images, name='search_images'),
    url(r'^all/$', views.all_images, name='allImages')
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)