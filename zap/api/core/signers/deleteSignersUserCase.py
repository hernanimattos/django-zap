from .models import Signer

class DeleteSignersUserCase():
    def delete_signers(self, document: int):
        Signer.objects.filter(document=document).delete()
        return None
        