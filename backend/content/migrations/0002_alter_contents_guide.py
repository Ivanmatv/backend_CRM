# Generated by Django 3.2.16 on 2024-03-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='guide',
            field=models.BooleanField(help_text='Введите руководство', verbose_name='Руководство'),
        ),
    ]