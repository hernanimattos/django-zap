
from .serializers import SignerSerializer
from .models import Signer
from .repository import SignerRepository

class CreateBulkSignersUseCase():
    signer_repository = SignerRepository()
    def execute(self, signers, document):
        existing_signers = Signer.objects.filter(document=document)
        existing_signer_emails = set(signer.email for signer in existing_signers)
        signers_response = []
        for signer_data in signers:
            if signer_data['email'] not in existing_signer_emails:
                signer = self.signer_repository.create(document=document, **signer_data)
                signers_response.append(signer)

        all_signers = list(existing_signers) + signers_response
   
        return SignerSerializer(all_signers, many=True).data
