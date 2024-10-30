from .models import Company

class CompanyRepository():
    def get_company_by_token(self,token):
        try:
            return Company.objects.get(api_token=token)
        except Company.DoesNotExist:
            return None
        
    def get_or_create(self, company):

        try:
            company_instance, created = Company.objects.get_or_create(**company)
            return company_instance
        except Company.DoesNotExist:
            return None
