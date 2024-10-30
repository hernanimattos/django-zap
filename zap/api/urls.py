from django.urls import path
from .views import create_document, get_document_by_id, delete_document_by_id, update_document

urlpatterns = [
    path('api/documents/', create_document, name='create-document'),
    path('api/documents/<int:id>/', get_document_by_id, name='get-document-by-id'),
    path('api/documents/delete/<int:id>/', delete_document_by_id, name='delete-document-by-id'),
    path('api/documents/update/', update_document, name='update-document'),
    # Outras URLs
]