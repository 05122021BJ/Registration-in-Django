# Generated by Django 4.2 on 2023-04-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('cpf', models.CharField('CPF', max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
