from django.db import models


class Merch(models.Model):
    """Model merchandise"""
    STATUS = (
        ('IN STOCK', 'В наличии'),
        ('OUT', 'Закончилось'),
    )
    SIZE = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    )
    size_foot = models.PositiveIntegerField(
        verbose_name='Размер обуви, см',
        default=None,
        null=True,
        blank=True
    )
    size_shirt = models.CharField(
        verbose_name='Размер одежды',
        max_length=10,
        choices=SIZE,
        null=True,
        blank=True
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
        verbose_name='Описание',
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField(
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
        verbose_name='Дата создания'
    )
    data_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    image = models.FileField(
        upload_to='media/image/',
        verbose_name='Изображения',
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self) -> str:
        return (f'{self.name} '
                f'{"(в наличии )" if self.status else "(закончилось)"}')


class Order(models.Model):
    """Model order"""

    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    cost = models.PositiveIntegerField(
        verbose_name='Стоймость'
    )
    count = models.PositiveIntegerField(
        verbose_name='Количество товара'
    )
    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    merchs = models.ManyToManyField(
        Merch,
        through='MerchOrder',
        related_name='merchs',
        verbose_name='Товары'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('pk',)

    def __str__(self) -> str:
        return f'{self.name}'


class MerchOrder(models.Model):
    """Model connection between merch and order"""
    merch = models.ForeignKey(
        Merch,
        related_name='merchorder',
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    order = models.ForeignKey(
        Order,
        related_name='merchorder',
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )

    class Meta:
        verbose_name = 'Заказ товара'
        verbose_name_plural = 'Заказы товаров'
        ordering = ('pk',)
        unique_together = ('merch', 'order')

    def __str__(self):
        return (f'{self.merch} - {self.order}')
