# Generated by Django 3.2.7 on 2021-10-02 23:46

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(db_index=True, help_text='Email used to login in the plataform and admin dashboard', max_length=254, unique=True, verbose_name='Email address')),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='Last name')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('picture', models.ImageField(blank=True, help_text='Profile picture', null=True, upload_to='accounts/user/', verbose_name='Picture')),
                ('alt_picture', models.CharField(blank=True, help_text='The text that represents the picture.', max_length=255, null=True, verbose_name='Alt picture')),
                ('is_active', models.BooleanField(default=True, help_text='The user is active?', verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, help_text='The user can access the admin dashboard?', verbose_name='Staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='The user can be a superuser?', verbose_name='Superuser status')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='This register is active? If set as no, will show in website!', verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='ProductUserAccessed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit', models.PositiveIntegerField(default=0, help_text='Number of access.', verbose_name='Hit')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_accessed_product', to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product User Accessed',
                'verbose_name_plural': 'Products User Accessed',
            },
        ),
        migrations.CreateModel(
            name='UserShopped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='This register is active? If set as no, will show in website!', verbose_name='Active')),
                ('products', models.ManyToManyField(related_name='user_shopped', to='products.Product', verbose_name='Products')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shopped', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Product Shopped',
                'verbose_name_plural': 'Products Shopped',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='This register is active? If set as no, will show in website!', verbose_name='Active')),
                ('products', models.ManyToManyField(related_name='user_favorite', to='products.Product', verbose_name='Products')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Product Favorite',
                'verbose_name_plural': 'Products Favorite',
            },
        ),
        migrations.CreateModel(
            name='UserAccessed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='This register is active? If set as no, will show in website!', verbose_name='Active')),
                ('products', models.ManyToManyField(related_name='user_accessed', through='accounts.ProductUserAccessed', to='products.Product', verbose_name='Products')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accessed', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Product Accessed',
                'verbose_name_plural': 'Products Accessed',
            },
        ),
        migrations.AddField(
            model_name='productuseraccessed',
            name='user_accessed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_user_accessed', to='accounts.useraccessed', verbose_name='Cart'),
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, help_text='This register is active? If set as no, will show in website!', verbose_name='Active')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_cart', to='accounts.cart', verbose_name='Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_products', to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Cart',
                'verbose_name_plural': 'Products Cart',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='cart', through='accounts.ProductCart', to='products.Product', verbose_name='Products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]