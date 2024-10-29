from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .createDocumentsUseCase import CreateDocumentUseCase

@api_view(['POST'])
def create_document(request):
    token = request.headers.get('Authorization').split(' ')[1]
    document =   CreateDocumentUseCase().execute(request.data, token)
 
    # todo: chamar a api do zap
    # criar o documento
    # pegar o retorno
    # buscar o documento atual
    # atualizar o documento com o retorno


    return Response(document, status=status.HTTP_201_CREATED)

