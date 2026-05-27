from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Sushi', 'Sushi'),
        ('Ramen', 'Ramen'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks/Sake'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/', blank=True, null=True)
    category = models.CharField(max_length=50, default='Interior')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

