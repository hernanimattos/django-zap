from .models import Signer
class SignerRepository():
    def bulk_create(self, signers_bulk):
        Signer.objects.bulk_create(signers_bulk)
        return signers_bulk

    def get_by_document(self, document):
        return Signer.objects.filter(document=document)
    
    def create(self, document, signer_data):

        Signer.objects.get_or_create(document=document, **signer_data)
        
        return Signer.objects.get(document=document)
    
    def update(self, document, signer):
        return Signer.objects.update(document=document, **signer)
    
    def bulk_update(self, document, signers_new_data):
        current_signers = self.get_by_document(document)
        signer_update = []
        for signer_data in signers_new_data:
            signer = next((s for s in current_signers if s.email == signer_data['email']), None)
            if signer:
                for key, value in signer_data.items():
                    setattr(signer, key, value)
                signer.save()
                signer_update.append(signer)

        return self.get_by_document(document)
