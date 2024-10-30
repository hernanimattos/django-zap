from .models import Document
from api.core.signers.models import Signer
from api.core.signers.repository import SignerRepository

# import pdb  # noqa

class DocumentRepository:
 
    def create_document(self, data, company):
        # signers_data = data.pop('signers', [])
        # data.pop('url_pdf', None)  
        doc_data = {
            'company': company,
            **data,
        }
        document, created = Document.objects.get_or_create(**doc_data)

        return document

    def update_document(self, document_data, signers_to_update):
        document_data.pop('signers', [])

        document = Document.objects.get(id=document_data['id'])

        for key, value in document_data.items():
            setattr(document, key, value)
        document.save()
    
        return document
    
    def get_document_by_id(self):
        return Document.objects.get()