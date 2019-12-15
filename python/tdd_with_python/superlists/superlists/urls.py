from django.contrib import admin
from django.urls import path, include
from lists.views import home_page, view_list, new_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('lists/the-only-list-in-the-world/', view_list, name='view_list'),
    path('lists/new', new_list, name='new_list'),
]
