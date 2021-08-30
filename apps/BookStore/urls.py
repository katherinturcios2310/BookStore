from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('books/', books, name='books'),
    path('contact/', contact, name='contact'),
    path('library/', library, name='library'),
]