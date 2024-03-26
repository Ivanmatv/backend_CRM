# Generated by Django 3.2.16 on 2024-03-24 15:31

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merch', '0002_alter_merch_image'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambassador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(max_length=32, unique=True, verbose_name='Ник в телеграме')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=100, null=True, verbose_name='Отчество')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол')),
                ('course', models.CharField(choices=[('data_analyst', 'Аналитик данных'), ('data_scientist', 'Специалист по Data Science'), ('python_developer', 'Python-разработчик'), ('web_developer', 'Веб-разработчик'), ('qa', 'Инженер по тестированию (QA)'), ('ux_ui', 'UX/UI-дизайнер'), ('marketing', 'Маркетинг'), ('graphic_designer', 'Графический дизайнер'), ('middle_python', 'Middle Python'), ('c++', 'C++'), ('data_engineer', 'Инженер данных'), ('it-recruiter', 'IT-рекрутер'), ('management', 'Управление'), ('english', 'Английский'), ('critical_thinking', 'Критическое мышление'), ('work_communication', 'Рабочая коммуникация'), ('algorithms', 'Алгоритмы для разработчиков'), ('product_design', 'Продуктовый дизайн'), ('sql', 'SQL для работы с данными и аналитики'), ('java_developer', 'Java-разработчик'), ('illustrator', 'Коммерческий иллюстратор'), ('fullstack_developer', 'Фулстек разработчик'), ('go_developer', 'Продвинутый GO-разработчик'), ('devops', 'DevOps для эксплуатации и разработки'), ('ios_developer', 'IOS-разработчик'), ('business_analyst', 'Бизнес-аналитик'), ('product_manager', 'Продакт-менеджер для специалистов с опытом'), ('android_developer', 'Android-разработчик'), ('project_manager', 'Менеджер проектов')], max_length=25, verbose_name='Программа обучения')),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('postcode', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)], verbose_name='Индекс')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('education', models.CharField(max_length=255, verbose_name='Образование')),
                ('status', models.CharField(choices=[('active', 'Активный'), ('paused', 'На паузе'), ('not_amb', 'Не амбассадор'), ('undefined', 'Уточняется')], default='undefined', max_length=11, verbose_name='Статус')),
                ('work', models.CharField(max_length=255, verbose_name='Место работы')),
                ('purpose', models.CharField(choices=[('profession', 'Получение новой профессии, чтобы сменить работу'), ('knowledge', 'Углубление имеющихся знаний, чтобы использовать их в текущей работе'), ('other', 'Другое')], max_length=12, verbose_name='Цель обучения в Практикуме')),
                ('other', models.CharField(blank=True, max_length=255, null=True, verbose_name='Цель обучения (другое)')),
                ('social', models.URLField(blank=True, null=True, verbose_name='Ссылка на соцсеть')),
                ('shirt_size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=2, verbose_name='Размер одежды')),
                ('foot_size', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Размер обуви')),
                ('comments', models.TextField(blank=True, max_length=1000, null=True, verbose_name='О себе')),
                ('onboarding', models.BooleanField(default=False, verbose_name='Амбассадор прошел Онбординг')),
                ('guide', models.BooleanField(default=False, verbose_name='Амбассадор выполнил задания из Гайда')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ambassador', to='content.content', verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Амбассадор',
                'verbose_name_plural': 'Амбассадор',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_end', models.DateTimeField(null=True, validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2024, 3, 24, 15, 31, 44, 84460, tzinfo=utc))], verbose_name='Дата окончания действия')),
                ('name', models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3), django.core.validators.RegexValidator(regex='^[A-Z0-9]+$')], verbose_name='Промокод')),
                ('status', models.BooleanField(verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Промокод',
                'verbose_name_plural': 'Промокоды',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='WorkIt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_blog', models.BooleanField(default=False, verbose_name='Вести блог')),
                ('is_community', models.BooleanField(default=False, verbose_name='Развивать сообщество')),
                ('is_articles', models.BooleanField(default=False, verbose_name='Писать статьи')),
                ('is_video', models.BooleanField(default=False, verbose_name='Снимать видео')),
                ('is_workshop', models.BooleanField(default=False, verbose_name='Знакомить коллег с ЯП')),
                ('is_advice', models.BooleanField(default=False, verbose_name='Консультировать по ЯП')),
                ('is_events', models.BooleanField(default=False, verbose_name='Выступать на мероприятиях')),
            ],
            options={
                'verbose_name': 'Желаемая деятельность',
                'verbose_name_plural': 'Желаемые виды деятельности',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='AmbassadorPromocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambassador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ambassador_promo', to='ambassadors.ambassador', verbose_name='Амбассадор')),
                ('promocode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promo_ambassador', to='ambassadors.promocode', verbose_name='Промокод')),
            ],
            options={
                'verbose_name': 'Промокод амбассадора',
                'verbose_name_plural': 'Промокоды амбассадоров',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='AmbassadorMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambassador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ambassador_merch', to='ambassadors.ambassador', verbose_name='Амбассадор')),
                ('merch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merch_ambassador', to='merch.merch', verbose_name='Мерч')),
            ],
            options={
                'verbose_name': 'Мерч амбассадора',
                'verbose_name_plural': 'Мерч амбассадоров',
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='ambassador',
            name='merch',
            field=models.ManyToManyField(related_name='merch', through='ambassadors.AmbassadorMerch', to='merch.Merch', verbose_name='Мерч'),
        ),
        migrations.AddField(
            model_name='ambassador',
            name='promocode',
            field=models.ManyToManyField(related_name='promocodes', through='ambassadors.AmbassadorPromocode', to='ambassadors.Promocode', verbose_name='Промокод'),
        ),
        migrations.AddField(
            model_name='ambassador',
            name='work_it',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_it', to='ambassadors.workit', verbose_name='Желаемая деятельность'),
        ),
    ]
