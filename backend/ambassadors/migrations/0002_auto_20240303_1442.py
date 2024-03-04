# Generated by Django 3.2.16 on 2024-03-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassadors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ambassador',
            old_name='promocode_id',
            new_name='promocode',
        ),
        migrations.RenameField(
            model_name='ambassadormerch',
            old_name='ambassador_id',
            new_name='ambassador',
        ),
        migrations.RenameField(
            model_name='ambassadormerch',
            old_name='merch_id',
            new_name='merch',
        ),
        migrations.RenameField(
            model_name='ambassadorpromocode',
            old_name='ambassador_id',
            new_name='ambassador',
        ),
        migrations.RenameField(
            model_name='ambassadorpromocode',
            old_name='promocode_id',
            new_name='promocode',
        ),
        migrations.AddField(
            model_name='ambassador',
            name='merch',
            field=models.ManyToManyField(related_name='merch', through='ambassadors.AmbassadorMerch', to='ambassadors.Merch', verbose_name='Мерч'),
        ),
    ]
