# Generated by Django 4.1.7 on 2023-04-12 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('sale_percent', models.PositiveSmallIntegerField(default=0)),
                ('best_seller', models.BooleanField(default=False)),
                ('price', models.FloatField(default=0)),
                ('pub_year', models.PositiveIntegerField(null=True)),
                ('page_size', models.PositiveIntegerField(null=True)),
                ('lang', models.CharField(choices=[('uzbek', 'Uzbek'), ('english', 'English'), ('russian', 'Russian')], max_length=50)),
                ('file', models.FileField(upload_to='')),
                ('image', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='books.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.category')),
            ],
        ),
    ]
