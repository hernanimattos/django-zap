from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .createDocumentsUseCase import CreateDocumentUseCase
from .getDocumentByIdUseCase import GetDocumentsUseCase
from .deleteDocumentUseCase import DeleteDocumentUseCase
from .updateDocumentUseCase import UpdateDocumentUseCase

@api_view(['POST'])
def create_document(request):
    token = request.headers.get('Authorization').split(' ')[1]

    document = CreateDocumentUseCase().execute(request.data, token)
 
    return Response(document, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_document_by_id(request, id):
    token = request.headers.get('Authorization').split(' ')[1]

    document = GetDocumentsUseCase().execute(id, token)

    return Response(document, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_document_by_id(request, id):
    token = request.headers.get('Authorization').split(' ')[1]
 
    DeleteDocumentUseCase().execute(id, token)

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_document(request):
    token = request.headers.get('Authorization').split(' ')[1]
 
    document = UpdateDocumentUseCase().execute(request.data, token)
    return Response(document, status=status.HTTP_200_OK)



