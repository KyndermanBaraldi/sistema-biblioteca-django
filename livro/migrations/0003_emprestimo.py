# Generated by Django 4.1.7 on 2023-04-30 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0002_alter_livros_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.livros')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'verbose_name': 'Emprestimo',
                'verbose_name_plural': 'Emprestimos',
            },
        ),
    ]
