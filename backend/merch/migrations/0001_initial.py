# Generated by Django 3.2.16 on 2024-03-08 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_foot', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Размер обуви, см')),
                ('size_shirt', models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=10, null=True, verbose_name='Размер одежды')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('status', models.CharField(choices=[('IN STOCK', 'В наличии'), ('OUT', 'Закончилось')], max_length=50, verbose_name='Наличие')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
                ('data_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('data_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('image', models.FileField(blank=True, default=None, null=True, upload_to='media/image/', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MerchOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchorder', to='merch.merch', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заказ товара',
                'verbose_name_plural': 'Заказы товаров',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('cost', models.PositiveIntegerField(verbose_name='Стоймость')),
                ('count', models.PositiveIntegerField(verbose_name='Количество товара')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('merchs', models.ManyToManyField(related_name='merchs', through='merch.MerchOrder', to='merch.Merch', verbose_name='Товары')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='merchorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchorder', to='merch.order', verbose_name='Заказ'),
        ),
        migrations.AlterUniqueTogether(
            name='merchorder',
            unique_together={('merch', 'order')},
        ),
    ]
