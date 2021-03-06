# Generated by Django 4.0.5 on 2022-06-14 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Nomi')),
                ('author', models.CharField(max_length=50, verbose_name='Muallif')),
                ('snippet', models.CharField(max_length=512, verbose_name='Qisqacha')),
                ('description', models.TextField(verbose_name='Malumot')),
                ('images', models.ImageField(upload_to='', verbose_name='Rasm')),
                ('language', models.CharField(max_length=50, verbose_name='Til')),
                ('shirft', models.CharField(max_length=20, verbose_name='Yozuv')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ism')),
                ('text', models.TextField(verbose_name='Fikr')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='booksapi.book', verbose_name='Kitob')),
            ],
        ),
    ]
