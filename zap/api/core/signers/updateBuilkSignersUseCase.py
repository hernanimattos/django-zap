from .repository import SignerRepository
from .serializers import SignerSerializer

class UpdateBulkSignersUseCase():
    signer_repository = SignerRepository()

    def execute(self, documents, signers):
        signers = self.signer_repository.bulk_update(documents, signers)
        return SignerSerializer(signers,many=True).data