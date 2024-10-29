from .models import Document
from api.core.signers.models import Signer
import pdb  # noqa

class DocumentRepository:
    
    def create_document(self, data, company):
        signers_data = data.pop('signers', [])
        data.pop('url_pdf', None)
        doc_data = {
            'company': company,
            **data,
        }

        pdb.set_trace()  
        document, created = Document.objects.get_or_create(**doc_data)
        signers = []
        for signer_data in signers_data:
            signer = Signer.objects.get_or_create(document=document, **signer_data)
            signers.append(signer)
        document.signers.set(signers)
        return document

    def update_document(self, document_data):
        signers_data = document_data.pop('signers', [])
        document_id = document_data.pop('id')

        # Recupere o documento existente
        document = Document.objects.get(id=document_id)
        
        # Atualize os campos do documento
        for key, value in document_data.items():
            setattr(document, key, value)
        
        # Salve o documento atualizado
        document.save()

        # Atualize ou crie signers
        signers = []
        for signer_data in signers_data:
            signer, created = Signer.objects.update_or_create(
                document=document,
                defaults=signer_data
            )
            signers.append(signer)
        
        # Atribua signers ao documento
        document.signers.set(signers)
        
        return document