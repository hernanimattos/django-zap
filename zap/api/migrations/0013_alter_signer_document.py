# Generated by Django 5.1.2 on 2024-10-29 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_signer_document_alter_document_signer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signer',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='signers', to='api.document'),
        ),
    ]
