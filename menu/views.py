from django.shortcuts import render
from .models import MenuItem

def menu_list(request):
    sushi_items = MenuItem.objects.filter(category='Sushi')
    ramen_items = MenuItem.objects.filter(category='Ramen')
    dessert_items = MenuItem.objects.filter(category='Desserts')
    drink_items = MenuItem.objects.filter(category='Drinks')
    
    context = {
        'sushi_items': sushi_items,
        'ramen_items': ramen_items,
        'dessert_items': dessert_items,
        'drink_items': drink_items,
    }
    return render(request, 'menu/menu_list.html', context)
