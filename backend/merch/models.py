from django.db import models


class Merch(models.Model):
    """Model merchandise"""
    STATUS = (
        ('IN STOCK', 'В наличии'),
        ('OUT', 'Закончилось'),
    )

    merch_id = models.PositiveIntegerField(primary_key=True)
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
        verbose_name='Категоия'
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

    def __str__(self) -> str:
        return f'{self.name}'


class Order(models.Model):
    """Model order"""

    order_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(
        max_length=100,
        verbose_name='Имя амбассадора'
    )
    cost = models.FloatField(
        verbose_name='Цена мерча'
    )
    count = models.IntegerField(
        verbose_name='Количество мерча'
    )
    date_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    merch = models.CharField()

    def __str__(self) -> str:
        return f'{self.name}'


class MerchOrder(models.Model):
    """Model connection between merch and order"""
    merch_id = models.ForeignKey(
        Merch,
        related_name='merch_merch',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    merch = models.ForeignKey(
        Order,
        related_name='merch_merch',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
