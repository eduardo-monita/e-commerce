# Generated by Django 3.2.7 on 2021-10-23 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211023_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='origin_destination_zip_codezip_code',
            new_name='destination_zip_code',
        ),
    ]
