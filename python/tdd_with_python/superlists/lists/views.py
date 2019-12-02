from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
    """
    return render(request, 'home.html', {
        'new_item_text': new_item_text
    })
    """
