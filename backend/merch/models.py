from django.db import models


class Merch(models.Model):
    """Model merchandise"""
    STATUS = (
        ('IN STOCK', 'В наличии'),
        ('OUT', 'Закончилось'),
    )
    # merch_id = models.AutoField(primary_key=True)
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
        auto_now_add=True,
        verbose_name='Дата обновления'
    )
    image = models.FileField(
        upload_to='merchs/media/image/',
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
        return (f'Товар {self.name}'
                f'{"(в наличии)" if self.status else "(закончилось)"}')


class Order(models.Model):
    """Model order"""

    # order_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=100,
        verbose_name='Имя амбассадора'
    )
    cost = models.FloatField(
        verbose_name='Цена товара'
    )
    count = models.IntegerField(
        verbose_name='Количество товара'
    )
    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
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
        related_name='merch_merch',
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Order,
        related_name='merch_merch',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Заказ товара'
        verbose_name_plural = 'Заказы товаров'
        ordering = ('pk',)

    def __str__(self):
        return (f'{self.merch_id} - {self.order_id}')
