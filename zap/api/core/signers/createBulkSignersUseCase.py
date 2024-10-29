from .repository import SignerRepository
from .serializers import SignerSerializer
from .models import Signer

class CreateBulkSignersUseCase():
    signers_repository = SignerRepository()
    serializer_class = SignerSerializer

    def execute(self, signers):
        serializer = self.get_serializer(data=signers, many=True)
        serializer.is_valid(raise_exception=True)
        signers_bulk = [Signer(**sign) for sign in serializer.validated_data]
        signers = self.signers_repository.bulk_create(signers_bulk)

        return signers
