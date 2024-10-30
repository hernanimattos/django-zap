from .serializers import SignerSerializer
from .models import Signer
class UpdateBulkSignersUseCase():
  

    def execute(self, document, signers):
        for signer_data in signers:
           find_signer  =  Signer.objects.filter(document=document, email=signer_data['email']).first()
           if find_signer:
                signer_data.pop('id', None)
                Signer.objects.filter(id=find_signer.id).update(**signer_data)

        return SignerSerializer(Signer.objects.filter(document=document), many=True).data