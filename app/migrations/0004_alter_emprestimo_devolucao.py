# Generated by Django 5.1.3 on 2024-11-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_autor_options_alter_editora_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='devolucao',
            field=models.DateField(default='1600-12-01'),
        ),
    ]
