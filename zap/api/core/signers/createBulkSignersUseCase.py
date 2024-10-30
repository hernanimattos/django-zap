from .serializers import SignerSerializer
from .models import Signer
class CreateBulkSignersUseCase():

    def execute(self, signers, document):
        existing_signers = Signer.objects.filter(document=document)
        existing_signer_emails = set(signer.email for signer in existing_signers)
        for signer_data in signers:
            if signer_data['email'] not in existing_signer_emails:
                print(f'Creating signer with email {signer_data["email"]}')
                Signer.objects.create(document=document, **signer_data)
            else:
                print(f'Signer with email {signer_data["email"]} already exists in the document')
