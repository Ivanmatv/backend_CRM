from django.db import models
from django.core.validators import MaxValueValidator
from .validators import validate_domain
# from merches.models import Merch
# from tasks.models import Content


GENDERS = [
    ('M', 'Мужской'),
    ('F', 'Женский'),
]

COURSES = [
    ('data_analyst', 'Аналитик данных'),
    ('data_scientist', 'Специалист по Data Science'),
    ('python_developer', 'Python-разработчик'),
    ('web_developer', 'Веб-разработчик'),
    ('qa', 'Инженер по тестированию (QA)'),
    ('ux_ui', 'UX/UI-дизайнер'),
    ('marketing', 'Маркетинг'),
    ('graphic_designer', 'Графический дизайнер'),
    ('middle_python', 'Middle Python'),
    ('c++', 'C++'),
    ('data_engineer', 'Инженер данных'),
    ('it-recruiter', 'IT-рекрутер'),
    ('management', 'Управление'),
    ('english', 'Английский'),
    ('critical_thinking', 'Критическое мышление'),
    ('work_communication', 'Рабочая коммуникация'),
    ('algorithms', 'Алгоритмы для разработчиков'),
    ('product_design', 'Продуктовый дизайн'),
    ('sql', 'SQL для работы с данными и аналитики'),
    ('java_developer', 'Java-разработчик'),
    ('illustrator', 'Коммерческий иллюстратор'),
    ('fullstack_developer', 'Фулстек разработчик'),
    ('go_developer', 'Продвинутый GO-разработчик'),
    ('devops', 'DevOps для эксплуатации и разработки'),
    ('ios_developer', 'IOS-разработчик'),
    ('business_analyst', 'Бизнес-аналитик'),
    ('product_manager', 'Продакт-менеджер для специалистов с опытом'),
    ('android_developer', 'Android-разработчик'),
    ('project_manager', 'Менеджер проектов'),
]


STATUSES = [
    ('active', 'Активный'),
    ('paused', 'На паузе'),
    ('not_amb', 'Не амбассадор'),
    ('undefined', 'Уточняется'),
]


class Promocod(models.Model):
    date_start = models.models.DateTimeField(
        'Дата начала',
        auto_now=True,
        auto_now_add=False
    )
    date_end = models.models.DateTimeField(
        'Дата окончания',
        auto_now=False,
        auto_now_add=False
    )
    name = models.CharField(
        'Промокод',
        max_length=32,
    )
    status = models.models.BooleanField(
        'Статус промокода',
    )


class Ambassador(models.Model):
    ambassador_telegram = models.CharField(
        'Ник в телеграме',
        primary_key=True,
        max_length=32,
    )
    first_name = models.CharField(
        'Имя',
        max_length=100,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100,
    )
    second_name = models.CharField(
        'Отчество',
        max_length=100,
    )
    gender = models.CharField(
        'Пол',
        max_length=1,
        choices=GENDERS,
    )
    course = models.CharField(
        'Программа обучения',
        max_length=25,
        choices=COURSES,
    )
    country = models.CharField(
        'Страна',
        max_length=100,
    )
    city = models.CharField(
        'Город',
        max_length=100,
    )
    address = models.CharField(
        'Адрес',
        max_length=100,
    )
    postcode = models.models.PositiveIntegerField(
        'Индекс',
        validators=[MaxValueValidator(100)],
    )
    email = models.models.EmailField(
        'Email',
        validators=[validate_domain],
    )
    phone = models.models.CharField(
        'Телефон',
        max_length=25,
    )
    education = models.models.CharField(
        'Образование',
        max_length=256,
    )
    status = models.CharField(
        'Статус',
        choices=STATUSES,
        max_length=11,
    )
    work = models.models.CharField(
        'Место работы',
        max_length=256,
    )
    promocod = models.ManyToManyField(
        Promocod,
        through='AmbassadorPromocod',
        verbose_name='Промокод',
        related_name='promocod',
        on_delete=models.CASCADE
    )
    # content_id = models.models.ForeignKey(
    #     Content,
    #     verbose_name=('Контент'),
    #     on_delete=models.CASCADE
    # )
    # amb_merch = models.ManyToManyField(
    #     Merch,
    #     through='',
    #     verbose_name=('Мерч'),
    #     on_delete=models.CASCADE
    # )

    class Meta:
        verbose_name = 'Амбассадор'
        verbose_name_plural = 'Амбассадор'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class AmbassadorPromocod(models.Model):
    ambassador_telegram = models.ForeignKey(
        Ambassador,
        verbose_name='Телеграм амбассадора',
        on_delete=models.CASCADE,
        related_name='ambassador_tg'
    )
    promocod_id = models.ForeignKey(
        Promocod,
        verbose_name='Промокод',
        on_delete=models.CASCADE,
        related_name='ambassador_tg'
    )
