from django.urls import path
from lists.views import view_list, new_list, add_item

urlpatterns = [
    path('<int:id>/', view_list, name='view_list'),
    path('<int:id>/add_item', add_item, name='add_item'),
    path('new', new_list, name='new_list'),
]
