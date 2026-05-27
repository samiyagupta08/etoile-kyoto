from django.shortcuts import render
from menu.models import MenuItem, Review, GalleryImage

def index(request):
    featured_dishes = MenuItem.objects.filter(featured=True)[:4]
    testimonials = Review.objects.all().order_by('-created_at')[:3]
    ambiance_images = GalleryImage.objects.filter(category='Interior')[:4]
    
    context = {
        'featured_dishes': featured_dishes,
        'testimonials': testimonials,
        'ambiance_images': ambiance_images,
    }
    return render(request, 'home/index.html', context)

def about(request):
    gallery_images = GalleryImage.objects.all()
    context = {
        'gallery_images': gallery_images,
    }
    return render(request, 'home/about.html', context)
