from django.db import models


class Content(models.Model):

    STATUS = (
        ('IN PROGRESS', 'В работе'),
        ('PAUSE', 'Пауза'),
        ('DONE', 'Закончил')
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название контента',
        help_text='Введите название контента')
    platform = models.CharField(
        max_length=200,
        verbose_name='Название платформы',
        help_text='Введите название платформы',
    )
    link = models.URLField(
        verbose_name='Ссылка',
        help_text='Введите ссылку на контент',
    )
    guide = models.BooleanField(
        verbose_name='Руководство',
        help_text='Введите руководство'
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

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенты'

    def __str__(self):
        return self.name
