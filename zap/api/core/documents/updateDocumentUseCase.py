from .repository import DocumentRepository
from .serializers import DocumentSerializer
from api.core.signers.updateBuilkSignersUseCase import UpdateBulkSignersUseCase

class UpdateDocumentUseCase:
    document_repository =DocumentRepository()
    update_bulk_signers_use_case = UpdateBulkSignersUseCase()
    def execute(self, document, token):
        document_response = self.document_repository.update_document(document)
        signers_data = document.get('signers', [])
        signers = self.update_bulk_signers_use_case.execute(document_response, signers_data)

        return {**document, 'signers': signers}