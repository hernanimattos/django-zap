from .models import Signer
class SignerRepository():
    def create(self, signers_bulk):
        Signer.objects.bulk_create(signers_bulk)
        return signers_bulk
