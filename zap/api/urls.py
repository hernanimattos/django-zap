from django.urls import path
from .views import create_document

urlpatterns = [
    path('api/documents/', create_document, name='create-document'),
    # Outras URLs
]