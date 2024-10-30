from .repository import DocumentRepository
from .serializers import DocumentSerializer
from api.core.signers.listSignersUseCase import ListSignersUseCase

class GetDocumentsUseCase:
    document_repository = DocumentRepository()
    signer_list_use_case = ListSignersUseCase()
    
    def execute(self, document_id: str, token: str):
        document =  DocumentSerializer(self.document_repository.get_document_by_id(document_id)).data
        document.pop('signers', None)
        signers = self.signer_list_use_case.execute(document_id)
        return {**document, 'signers': signers}

        # return document   