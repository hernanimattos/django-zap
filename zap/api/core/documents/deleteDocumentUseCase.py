from .repository import DocumentRepository

class DeleteDocumentUseCase():
    document_repository = DocumentRepository()

    def execute(self, document_id, token: str):

        self.document_repository.delete_document(document_id)