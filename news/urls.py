from django.urls import path
from .views import index, create, details, edit, delete


urlpatterns = [
    path('', index),
    path('index', index),
    path('create', create),
    path('details', details),
    path('edit', edit),
    path('delete', delete)
]
