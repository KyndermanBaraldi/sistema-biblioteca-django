# Generated by Django 4.1.7 on 2023-04-29 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
    ]