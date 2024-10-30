from .models import Signer
from typing import List
from .serializers import SignerSerializer

class ListSignersUseCase:

    def execute(self, document):
        signers = Signer.objects.filter(document=document)
        return SignerSerializer(signers, many=True).data