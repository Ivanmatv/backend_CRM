# Generated by Django 3.2.16 on 2024-03-03 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambassadors', '0002_auto_20240303_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambassador',
            name='promocode',
            field=models.ManyToManyField(related_name='promocodes', through='ambassadors.AmbassadorPromocode', to='ambassadors.Promocode', verbose_name='Промокод'),
        ),
        migrations.AlterField(
            model_name='ambassadormerch',
            name='ambassador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ambassador_merch', to='ambassadors.ambassador', verbose_name='Амбассадор'),
        ),
        migrations.AlterField(
            model_name='ambassadormerch',
            name='merch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merch_ambassador', to='ambassadors.merch', verbose_name='Мерч'),
        ),
        migrations.AlterField(
            model_name='ambassadorpromocode',
            name='ambassador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ambassador_promo', to='ambassadors.ambassador', verbose_name='Амбассадор'),
        ),
        migrations.AlterField(
            model_name='ambassadorpromocode',
            name='promocode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promo_ambassador', to='ambassadors.promocode', verbose_name='Промокод'),
        ),
    ]