from django.db import models
from api.core.documents.models import Document


class Signer(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255, null=False, blank=True)
    status = models.CharField(max_length=50, null=False, default='')
    name = models.CharField(max_length=255, null=False, blank=True, default='')
    email = models.EmailField(max_length=255, null=False, blank=True, default='')
    external_id = models.CharField(max_length=255, blank=True, null=True, default='')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='signers', null=True)

    def __str__(self):
        return self.name
