from django.utils.text import slugify
import string, random
from .models import Feeds

def generate_random_string(N): 
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res

def slug_generater(text):
    new_slug = slugify(text)
    if Feeds.objects.filter(slug = new_slug).first():
        return slug_generater(text + generate_random_string(5))
    return new_slug