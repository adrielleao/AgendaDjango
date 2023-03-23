# Generated by Django 4.1.7 on 2023-03-18 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('usuario', models.CharField(max_length=20)),
            ],
        ),
    ]
