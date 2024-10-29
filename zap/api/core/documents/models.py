from django.db import models
from api.core.company.models import Company

class Document(models.Model):
    # id = models.AutoField(primary_key=True)
    openID = models.IntegerField(null=False, blank=True, default=0)
    token = models.CharField(max_length=255, null=False, blank=True, default='')
    name = models.CharField(max_length=255, null=False, blank=True, default='')
    status = models.CharField(max_length=50, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='document')
    externalID = models.CharField(max_length=255, blank=True, null=True)
    signer = models.ManyToManyField('Signer', related_name='documents')

    def __str__(self):
        return self.name
    
# (null, 0, , My PDF Contract, , 2024-10-28 21:54:44.419992+00, 2024-10-28 21:54:44.420038+00, null, 2).
