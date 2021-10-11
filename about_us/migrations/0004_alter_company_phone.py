# Generated by Django 3.2.7 on 2021-10-11 01:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0003_alter_company_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='Invalid phone number', regex='\\(\\d{2,}\\) \\d{4,}\\-\\d{4}')], verbose_name='Phone number'),
        ),
    ]
