# Generated by Django 5.2 on 2025-04-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('endereco', models.TextField()),
            ],
        ),
    ]
