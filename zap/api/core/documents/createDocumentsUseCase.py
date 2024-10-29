from .serializers import DocumentSerializer
from api.core.company.getCompanyUseCase import GetCompanyUseCase
from .repository import DocumentRepository
from api.core.zapsign.createDocumentZapSignUseCase import CreateDocumentZapSignUseCase



class CreateDocumentUseCase():
    use_company_case = GetCompanyUseCase()
    document_repository = DocumentRepository()
    zap_sign_use_case = CreateDocumentZapSignUseCase()
    
    def execute(self, data, token):

        data_clone = data.copy()
      
        company = self.use_company_case.validate_token(token)
  
        # todo: chamar a api do zap
        # criar o documento
        # pegar o retorno
        # buscar o documento atual
        # atualizar o documento com o retorno
        # SignerSerializer(data=response_zap_sign.pop('signers'), many=True).data


        if not company:
            return {'errors': ['Invalid token']}
        
        print('company-----', data)
        
        document_created = self.document_repository.create_document(data, company)
        
        print('document_created', document_created)
        response_zap_sign = self.zap_sign_use_case.execute(data_clone, token)

        signers_to_update = [{'name':signer['name'], 'token':signer['token'], 'email' : signer['email'], 'status':signer['status'] } for signer in response_zap_sign['signers']]
       
        data_to_update = {
            'id':document_created['id'],
            'status':response_zap_sign['status'], 
            'name':response_zap_sign['name'],
            'openID':response_zap_sign['open_id'],
            'externalID':response_zap_sign['external_id'],
            'token':response_zap_sign['token'], 
            'signers':signers_to_update
            }
     
        # document_created = self.document_repository.update_document(data_to_update)

        return DocumentSerializer(data_to_update).data


        # return DocumentSerializer(document_created).data
        # return {'errors': signers_serializer.errors}