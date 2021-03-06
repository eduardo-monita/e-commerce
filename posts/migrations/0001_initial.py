# Generated by Django 3.2.7 on 2021-10-02 23:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='This register is active? If set as no, will show in website!', verbose_name='Active')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('picture', models.ImageField(upload_to='posts/author/', verbose_name='Picture')),
                ('alt_picture', models.CharField(blank=True, help_text='The text that represents the picture.', max_length=255, null=True, verbose_name='Alt picture')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='This register is active? If set as no, will show in website!', verbose_name='Active')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=255, verbose_name='SubTitle')),
                ('image', models.ImageField(upload_to='posts/post', verbose_name='Image')),
                ('alt_image', models.CharField(blank=True, help_text='The text that represents the image.', max_length=255, null=True, verbose_name='Alt image')),
                ('summary', models.CharField(help_text='This field is to show in the lists, a summary of post.', max_length=510, verbose_name='Summary')),
                ('body', ckeditor.fields.RichTextField(help_text='Body of post, save in html format.', verbose_name='Body')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='posts.author', verbose_name='Athor')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
