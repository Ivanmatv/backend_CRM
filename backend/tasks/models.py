from datetime import date

from django.db import models

from ambassadors.models import Ambassador


class Tasks(models.Model):

    STATUS = (
        ('IN PROGRESS', 'В работе'),
        ('PAUSE', 'Пауза'),
        ('DONE', 'Закончил')
    )
    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название задачи',
        help_text='Введите название задачи')
    date_start = models.DateField(
        default=date.today,
    )
    date_end = models.DateField(
        default=date.today,
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание'
    )
    status = models.CharField(
        max_length=50,
        verbose_name='Статус контента',
        help_text='Выберите статус',
        choices=STATUS
    )
    user_id = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name='Автор задачи',
        help_text='Пользователь, написавший задачу',
        related_name='tasks'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
