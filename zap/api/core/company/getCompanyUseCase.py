from api.core.company.repository import CompanyRepository

class GetCompanyUseCase():
    company_repository= CompanyRepository()
    def validate_token(self, token):

        comapny_to_create = {
            'name':'Zap',
            'api_token': token

        }
      
        company =  self.company_repository.get_or_create(comapny_to_create)
        if not company or not token:
            return {'errors': ['Invalid token']}
        return company