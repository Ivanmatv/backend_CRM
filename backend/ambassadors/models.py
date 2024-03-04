from django.db import models
# from django.core.validators import MaxValueValidator
# from merch.models import Merch
# from tasks.models import Content


class Merch(models.Model):
    """Model merchandise"""
    STATUS = (
        ('IN STOCK', 'В наличии'),
        ('OUT', 'Закончилось'),
    )

    size = models.PositiveIntegerField(
        verbose_name='Размер'
    )
    price = models.FloatField(
        verbose_name='Цена'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    desc = models.CharField(
        max_length=200,
        verbose_name='Описание'
    )
    quantity = models.IntegerField(
        verbose_name='Количество',
    )
    status = models.CharField(
        max_length=50,
        verbose_name='Наличие',
        choices=STATUS
    )
    category = models.CharField(
        max_length=50,
        verbose_name='Категория'
    )
    data_creation = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания'
    )
    data_update = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата обновления'
    )
    image = models.FileField(
        upload_to='merchs/media/image/',
        verbose_name='Изображения'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self) -> str:
        return (f'Товар {self.name}'
                f'{"(в наличии)" if self.status else "(закончилось)"}')


class Promocode(models.Model):
    date_start = models.DateTimeField(
        'Дата начала',
        auto_now_add=True
    )
    date_end = models.DateTimeField(
        'Дата окончания',
        auto_now=False,
        auto_now_add=False
    )
    name = models.CharField(
        'Промокод',
        max_length=32,
        unique=True
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

    STATUSES = [
        ('active', 'Активный'),
        ('paused', 'На паузе'),
        ('not_amb', 'Не амбассадор'),
        ('undefined', 'Уточняется'),
    ]

    telegram = models.CharField(
        'Ник в телеграме',
        max_length=32,
        unique=True
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
    # postcode = models.PositiveIntegerField(
    #     'Индекс',
    #     validators=[MaxValueValidator(999999)],
    # )
    email = models.EmailField(
        'Email',
    )
    phone = models.CharField(
        'Телефон',
        max_length=25,
    )
    education = models.CharField(
        'Образование',
        max_length=256,
    )
    status = models.CharField(
        'Статус',
        choices=STATUSES,
        max_length=11,
        default='undefined',
    )
    work = models.CharField(
        'Место работы',
        max_length=256,
    )
    promocode = models.ManyToManyField(
        Promocode,
        through='AmbassadorPromocode',
        verbose_name='Промокод',
        related_name='promocodes'
    )
    # content = models.models.ForeignKey(
    #     Content,
    #     verbose_name=('Контент'),
    #     on_delete=models.CASCADE
    # )
    merch = models.ManyToManyField(
        Merch,
        through='AmbassadorMerch',
        verbose_name='Мерч',
        related_name='merch'
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
        related_name='ambassador_promo'
    )
    promocode = models.ForeignKey(
        Promocode,
        verbose_name='Промокод',
        on_delete=models.CASCADE,
        related_name='promo_ambassador'
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
        related_name='merch_ambassador'
    )
    ambassador = models.ForeignKey(
        Ambassador,
        verbose_name='Амбассадор',
        on_delete=models.CASCADE,
        related_name='ambassador_merch'
    )

    class Meta:
        verbose_name = 'Мерч амбассадора'
        verbose_name_plural = 'Мерч амбассадоров'
        ordering = ('pk',)

    def __str__(self):
        return (f'{self.merch} - {self.ambassador}')
