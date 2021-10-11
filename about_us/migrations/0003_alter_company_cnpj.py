# Generated by Django 3.2.7 on 2021-10-10 23:32

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_auto_20211010_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(db_index=True, max_length=18, unique=True, verbose_name='CNPJ'),
        ),
    ]
