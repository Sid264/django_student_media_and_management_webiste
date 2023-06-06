from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Student Media"
admin.site.site_title = "Student Media Admin Portal"
admin.site.index_title = "Welcome to Student Media" 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
    