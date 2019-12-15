from django.contrib import admin
from django.urls import path, include
from lists.views import home_page, view_list, new_list, add_item

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home_page),
    path('lists/<int:id>/', view_list, name='view_list'),
    path('lists/<int:id>/add_item', add_item, name='add_item'),
    path('lists/new', new_list, name='new_list'),
]
