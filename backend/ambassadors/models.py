from django.utils import timezone
from django.db import models
from django.core.validators import (MaxValueValidator,
                                    MinValueValidator,
                                    MinLengthValidator,
                                    RegexValidator)
from merch.models import Merch
# from tasks.models import Content, Task


class Promocode(models.Model):
    date_start = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    date_end = models.DateTimeField(
        'Дата окончания действия',
        validators=(MinValueValidator(limit_value=timezone.now()),),
        null=True,
    )
    name = models.CharField(
        'Промокод',
        max_length=32,
        validators=(MinLengthValidator(limit_value=3),
                    RegexValidator(regex=r'^[A-Z0-9]+$'),),
        unique=True,
    )
    status = models.BooleanField(
        'Активен',
    )

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
        ordering = ('pk',)

    def __str__(self):
        return (f'Промокод {self.name} '
                f'{"(активен)" if self.status else "(неактивен)"}')


class WorkIt(models.Model):
    is_blog = models.BooleanField(
        'Вести блог',
        default=False,
    )
    is_community = models.BooleanField(
        'Развивать сообщество',
        default=False,
    )
    is_articles = models.BooleanField(
        'Писать статьи',
        default=False,
    )
    is_video = models.BooleanField(
        'Снимать видео',
        default=False,
    )
    is_workshop = models.BooleanField(
        'Знакомить коллег с ЯП',
        default=False,
    )
    is_advice = models.BooleanField(
        'Консультировать по ЯП',
        default=False,
    )
    is_events = models.BooleanField(
        'Выступать на мероприятиях',
        default=False,
    )

    class Meta:
        verbose_name = 'Желаемая деятельность'
        verbose_name_plural = 'Желаемые виды деятельности'
        ordering = ('pk',)

    def __str__(self):
        return (f'Желаемая деятельность {self.pk}')


class Ambassador(models.Model):
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

    PURPOSES = [
        ('profession', 'Получение новой профессии, чтобы сменить работу'),
        ('knowledge', 'Углубление имеющихся знаний, '
                      'чтобы использовать их в текущей работе'),
        ('other', 'Другое')
    ]

    STATUSES = [
        ('active', 'Активный'),
        ('paused', 'На паузе'),
        ('not_amb', 'Не амбассадор'),
        ('undefined', 'Уточняется'),
    ]

    SIZES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )

    telegram = models.CharField(
        'Ник в телеграме',
        max_length=32,
        unique=True,
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
        null=True,
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
    postcode = models.PositiveIntegerField(
        'Индекс',
        validators=[MaxValueValidator(999999)],
    )
    email = models.EmailField(
        'Email',
        unique=True,
    )
    phone = models.CharField(
        'Телефон',
        max_length=25,
    )
    education = models.CharField(
        'Образование',
        max_length=255,
    )
    status = models.CharField(
        'Статус',
        choices=STATUSES,
        max_length=11,
        default='undefined',
    )
    work = models.CharField(
        'Место работы',
        max_length=255,
    )
    purpose = models.CharField(
        'Цель обучения в Практикуме',
        choices=PURPOSES,
        max_length=12,
    )
    other = models.CharField(
        'Цель обучения (другое)',
        null=True,
        blank=True,
        max_length=255,
    )
    social = models.URLField(
        'Ссылка на соцсеть',
        null=True,
        blank=True,
    )
    shirt_size = models.CharField(
        'Размер одежды',
        choices=SIZES,
        max_length=2,
    )
    foot_size = models.PositiveSmallIntegerField(
        'Размер обуви',
        validators=(MaxValueValidator(50),),
    )
    work_it = models.ForeignKey(
        WorkIt,
        verbose_name='Желаемая деятельность',
        related_name='work_it',
        on_delete=models.CASCADE,
    )
    comments = models.TextField(
        'О себе',
        null=True,
        blank=True,
        max_length=1000,
    )
    promocode = models.ManyToManyField(
        Promocode,
        through='AmbassadorPromocode',
        verbose_name='Промокод',
        related_name='promocodes',
    )
    merch = models.ManyToManyField(
        Merch,
        through='AmbassadorMerch',
        verbose_name='Мерч',
        related_name='merch',
    )
    onboarding = models.BooleanField(
        'Амбассадор прошел Онбординг',
        default=False,
    )
    guide = models.BooleanField(
        'Амбассадор выполнил задания из Гайда',
        default=False,
    )
    # content = models.ManyToManyField(
    #     Content,
    #     through='AmbassadorContent',
    #     verbose_name='Контент',
    #     related_name='content'
    # )
    # task = models.models.ForeignKey(
    #     Task,
    #     verbose_name=('Задача'),
    #     on_delete=models.CASCADE
    # )
    create_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Амбассадор'
        verbose_name_plural = 'Амбассадор'
        ordering = ('pk',)

    def __str__(self):
        return f'Амбассадор {self.first_name} {self.last_name}'


class AmbassadorPromocode(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        verbose_name='Амбассадор',
        on_delete=models.CASCADE,
        related_name='ambassador_promo',
    )
    promocode = models.ForeignKey(
        Promocode,
        verbose_name='Промокод',
        on_delete=models.CASCADE,
        related_name='promo_ambassador',
    )

    class Meta:
        verbose_name = 'Промокод амбассадора'
        verbose_name_plural = 'Промокоды амбассадоров'
        ordering = ('pk',)

    def __str__(self):
        return (f'{self.promocode} - {self.ambassador}')


class AmbassadorMerch(models.Model):
    merch = models.ForeignKey(
        Merch,
        verbose_name='Мерч',
        on_delete=models.CASCADE,
        related_name='merch_ambassador',
    )
    ambassador = models.ForeignKey(
        Ambassador,
        verbose_name='Амбассадор',
        on_delete=models.CASCADE,
        related_name='ambassador_merch',
    )

    class Meta:
        verbose_name = 'Мерч амбассадора'
        verbose_name_plural = 'Мерч амбассадоров'
        ordering = ('pk',)

    def __str__(self):
        return (f'{self.merch} - {self.ambassador}')
