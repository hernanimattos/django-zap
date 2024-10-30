from .models import Document
from api.core.signers.models import Signer

# import pdb  # noqa

class DocumentRepository:
 
    def create_document(self, data, company):
 
        doc_data = {
            'company': company,
            **data,
        }
        document = Document.objects.create(**doc_data)

        return document

    def update_document(self, document_data):
        document_data.pop('signers', [])

        document = Document.objects.get(id=document_data['id'])

        for key, value in document_data.items():
            setattr(document, key, value)
        document.save()
    
        return document
    
    def get_document_by_id(self, document_id):
        return Document.objects.get(id=document_id)
