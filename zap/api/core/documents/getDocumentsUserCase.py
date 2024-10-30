from .repository import DocumentRepository

class GetDocumentsUseCase:
    docuemnt_repository = DocumentRepository()
    
    def get_document(self, document_id: str):
        return self.document_repository.get_document_by_id(document_id)