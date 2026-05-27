from django.db import models

class MenuItem(models.fields.Field):
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
