from django.urls import path
from .views import create_document, get_document_by_id

urlpatterns = [
    path('api/documents/', create_document, name='create-document'),
    path('api/documents/<int:id>/', get_document_by_id, name='get-document-by-id'),
    # Outras URLs
]