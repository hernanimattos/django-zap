from .serializers import DocumentSerializer
from .repository import DocumentRepository
from api.core.company.getCompanyUseCase import GetCompanyUseCase
from api.core.zapsign.createDocumentZapSignUseCase import CreateDocumentZapSignUseCase
from api.core.signers.createBulkSignersUseCase import CreateBulkSignersUseCase
from api.core.signers.updateBuilkSignersUseCase import UpdateBulkSignersUseCase
from .models import Document

class CreateDocumentUseCase():
    use_company_case = GetCompanyUseCase()
    document_repository = DocumentRepository()
    zap_sign_use_case = CreateDocumentZapSignUseCase()
    create_bulk_signers_use_case = CreateBulkSignersUseCase()
    update_bulk_signers__use_case = UpdateBulkSignersUseCase()
    
    def execute(self, data, token):
        data_clone = data.copy()
        data.pop('url_pdf', None)
        signers_data = data.pop('signers', [])
        company = self.use_company_case.validate_token(token)


        if not company:
            return {'errors': ['Invalid token']}
        
        doc_data = {
            'company': company,
            **data,
        }
        document_created = Document.objects.create(**doc_data)
        document_serializer = DocumentSerializer(document_created).data
    
        self.create_bulk_signers_use_case.execute(signers_data, document_created)
     
        response_zap_sign = self.zap_sign_use_case.execute(data_clone, token)
       
        signers_to_update = [
            {
                'id': signer.get('id'),
                'name': signer['name'], 
                'token': signer['token'], 
                'email' : signer['email'], 
                'status': signer['status'] 
            }  for signer in response_zap_sign['signers'] ]

   
        data_to_update = {
            'id':document_serializer['id'],
            'status':response_zap_sign['status'], 
            'name':response_zap_sign['name'],
            'openID':response_zap_sign['open_id'],
            'externalID':response_zap_sign['external_id'],
            'token':response_zap_sign['token'], 
            'signers':signers_to_update
            }

        document_updated = self.document_repository.update_document(data_to_update)
     
        updated_singers = self.update_bulk_signers__use_case.execute(document_updated, signers_to_update)
        document_serializer_serializer = DocumentSerializer(document_updated).data

        data_to_response = {
            **document_serializer_serializer,
            'signers': updated_singers
        }
        
        data_to_response.pop('signer', None)
       
        return data_to_response
