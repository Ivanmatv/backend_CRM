# Generated by Django 3.2.16 on 2024-03-21 18:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ambassadors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название задачи', max_length=150, unique=True, verbose_name='Название задачи')),
                ('date_start', models.DateField(default=datetime.date.today)),
                ('date_end', models.DateField(default=datetime.date.today)),
                ('description', models.TextField(help_text='Введите описание', verbose_name='Описание')),
                ('status', models.CharField(choices=[('IN PROGRESS', 'В работе'), ('PAUSE', 'Пауза'), ('DONE', 'Закончил')], help_text='Выберите статус', max_length=50, verbose_name='Статус контента')),
                ('user_id', models.ForeignKey(help_text='Пользователь, написавший задачу', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='ambassadors.ambassador', verbose_name='Автор задачи')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
