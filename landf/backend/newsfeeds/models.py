from django.db import models
from backend.accounts.models import Accounts
from .slug_generaters import slug_generater, category_slug_generater
from django.urls import reverse

class Feeds(models.Model):
    name = models.CharField(max_length=50, blank=True)
    item_name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=35,  null = True, blank = True)
    item_image = models.ImageField(upload_to='images/items/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location = models.CharField(max_length=35)
    time = models.CharField(max_length=20)
    descriptions = models.TextField()
    status = models.CharField(max_length=1)
    contact = models.CharField(max_length=20, blank=True)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        self.slug = slug_generater(self.item_name)
        super(Feeds, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('item_detail', args=[self.category.slug, self.slug])

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=25,  null = True, blank = True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = category_slug_generater(self.category_name)
        super(Category, self).save(*args, **kwargs)