# Generated by Django 5.1.2 on 2024-10-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_signer_document_alter_document_signers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='signers',
            field=models.ManyToManyField(related_name='document', to='api.signer'),
        ),
    ]
