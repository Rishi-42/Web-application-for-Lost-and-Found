from django.utils.text import slugify
import string, random


def generate_random_string(N): 
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res

def slug_generater(text):
    new_slug = slugify(text)
    from .models import Feeds
    if Feeds.objects.filter(slug = new_slug).first():
        return slug_generater(text + generate_random_string(5))
    return new_slug

def category_slug_generater(text):
    new_slug = slugify(text)
    return new_slug