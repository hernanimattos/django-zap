from api.shared.HttpProvider import HttpProvider
import os
from api.core.documents.serializers import DocumentSerializer

class CreateDocumentZapSignUseCase():
    http_provider = HttpProvider()
    document_serializer = DocumentSerializer()
    def execute(self, data, token):

        print(data)
        header = {'Authorization': 'Bearer ' + token}
        response = self.http_provider.post(os.getenv('ZAP_URL'), header, data)

        return response.json()