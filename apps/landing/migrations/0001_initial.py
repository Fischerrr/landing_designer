# Generated by Django 2.2 on 2019-12-23 16:28

import apps.landing.models
import ckeditor.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_ymap.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название блока')),
                ('template', models.PositiveSmallIntegerField(choices=[(1, 'Приветствие'), (2, 'О продукте'), (3, 'Особенности'), (4, 'Каталог'), (5, 'Форма помощи с выбором'), (6, 'Сервис'), (7, 'Премущества покупки'), (8, 'Ассортимент продукта'), (9, 'Форма дополнительных предложений'), (10, 'Блок со скрытым текстом'), (11, 'Карта'), (12, 'О компании'), (13, 'Сертификаты'), (14, 'Отзывы'), (15, 'Партнеры'), (16, 'Подписка на рассылку'), (17, 'Другие предложения')], db_index=True, verbose_name='Шаблон для блока')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='Подзаголовок')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Максимальное количество символов 1500', max_length=1500, null=True, verbose_name='Описание')),
                ('svg_background', models.FileField(blank=True, null=True, upload_to='landing/block/svg/', validators=[apps.landing.models.svg_validator], verbose_name='SVG изображение заднего фона')),
                ('text_button', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст для кнопки')),
                ('catalog_file', models.FileField(blank=True, help_text='Рекомендуется загружать PDF файлы', null=True, upload_to='landing/block/file/', verbose_name='Файл каталога')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блок',
            },
        ),
        migrations.CreateModel(
            name='BlockToLanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=False, verbose_name='Включен')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')),
                ('name_navigation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название пункта навигиции')),
                ('slug_navigation', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('use_navigation', models.BooleanField(default=False, verbose_name='Включить навигацию')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Block', verbose_name='Блок')),
            ],
            options={
                'verbose_name': 'Добавить блок',
                'verbose_name_plural': 'Добавление блоков',
                'ordering': ['position', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('incline_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Склоняемый заголовок для каталога')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Максимальное количество символов 1500', max_length=1500, null=True, verbose_name='Описание')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='landing/catalog/pdf/', validators=[apps.landing.models.pdf_validator], verbose_name='PDF файл')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталог',
                'ordering': ['priority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SpecificationProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название столбца продукта')),
                ('unit', ckeditor.fields.RichTextField(blank=True, max_length=255, null=True, verbose_name='Параметр продукта')),
            ],
            options={
                'verbose_name': 'Основная характеристика',
                'verbose_name_plural': 'Основные характеристики',
            },
        ),
        migrations.CreateModel(
            name='SpecificationProductTabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название столбца продукта')),
                ('unit', ckeditor.fields.RichTextField(blank=True, max_length=255, null=True, verbose_name='Параметр продукта')),
            ],
            options={
                'verbose_name': 'Дополнительная характеристика',
                'verbose_name_plural': 'Дополнительные характеристики',
            },
        ),
        migrations.CreateModel(
            name='TabsProductCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('template', models.PositiveSmallIntegerField(choices=[(1, 'Шаблон с изображением'), (2, 'Шаблон с галереей')], db_index=True, default=1, verbose_name='Шаблон для параметров продукта')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='landing/catalog/', verbose_name='Изображение')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Описание продукта каталога',
                'verbose_name_plural': 'Описание продуктов каталога',
            },
        ),
        migrations.CreateModel(
            name='Text2Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Максимальное количество символов 1500', max_length=1500, null=True, verbose_name='Описание')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='landing/block/', verbose_name='Изображение')),
                ('svg', models.FileField(blank=True, null=True, upload_to='landing/block/svg/', validators=[apps.landing.models.svg_validator], verbose_name='SVG изображение')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
                ('column_number', models.PositiveSmallIntegerField(choices=[(1, 'Первая колонка'), (2, 'Вторая колонка')], db_index=True, default=1, verbose_name='Номер колонки')),
                ('title_hide_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок скрытого текста')),
                ('hide_text', ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True, verbose_name='Скрытый текст')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Block', verbose_name='Блок')),
            ],
            options={
                'verbose_name': 'Текст для блока',
                'verbose_name_plural': 'Текст для блока',
                'ordering': ['priority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SpecificationsTabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_parameter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Параметр для группировки')),
                ('value', models.CharField(blank=True, max_length=100, null=True, verbose_name='Значение')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.SpecificationProductTabs', verbose_name='Параметр')),
                ('tabs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.TabsProductCatalog', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Параметр описания',
                'verbose_name_plural': 'Параметры для описания',
                'ordering': ['priority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SpecificationsForm2Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=False, verbose_name='Включен')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_select_first', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок первого селекта')),
                ('select_first', models.TextField(blank=True, help_text='Перечислите построчно необходимые параметры', null=True, verbose_name='Первый селект')),
                ('title_select_second', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок второго селекта')),
                ('select_second', models.TextField(blank=True, help_text='Перечислите построчно необходимые параметры', null=True, verbose_name='Второй селект')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Block', verbose_name='Блок')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductsCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('youtube', models.CharField(blank=True, max_length=255, null=True, verbose_name='YouTube ссылка')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
                ('json_param', django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True)),
                ('tabs', models.ManyToManyField(to='landing.TabsProductCatalog', verbose_name='Описание продукта')),
            ],
            options={
                'verbose_name': 'Продукт каталога',
                'verbose_name_plural': 'Продукты каталога',
                'ordering': ['priority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ParamColumnProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=100, null=True, verbose_name='Значение параметра')),
                ('column_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.SpecificationProduct', verbose_name='Столбцы продукта')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.ProductsCatalog', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Параметр колонки продукта',
                'verbose_name_plural': 'Параметры колонки продукта',
            },
        ),
        migrations.CreateModel(
            name='MultiSelectsForm2Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=False, verbose_name='Включен')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('select', models.TextField(blank=True, help_text='Перечислите построчно необходимые параметры', null=True, verbose_name='Параметры для выбора')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Block', verbose_name='Блок')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonoSelectsForm2Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=False, verbose_name='Включен')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('select', models.TextField(blank=True, help_text='Перечислите построчно необходимые параметры', null=True, verbose_name='Параметры для выбора')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Block', verbose_name='Блок')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(db_index=True, default=False, verbose_name='Включен')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('alt_url_site', models.URLField(blank=True, null=True, unique=True, verbose_name='Альтернативный url сайта')),
                ('type_product', models.CharField(max_length=255, verbose_name='Тип продукта')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
                ('main_color', models.CharField(default='#f4f4f4', max_length=7, verbose_name='Основной цвет')),
                ('second_color', models.CharField(default='#58504C', max_length=7, verbose_name='Второстепенный цвет')),
                ('accent_color', models.CharField(default='#F95D06', max_length=7, verbose_name='Акцентный цвет')),
                ('logo', models.FileField(blank=True, null=True, upload_to='landing/svg/', validators=[apps.landing.models.svg_validator], verbose_name='SVG логотип компнаии')),
                ('logo_mobile', models.FileField(blank=True, null=True, upload_to='landing/svg/', validators=[apps.landing.models.svg_validator], verbose_name='SVG логотип компании для мобильных экранов')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='landing/image/', verbose_name='Изображение приветствия')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон')),
                ('phone_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Подпись к телефону')),
                ('link_privacy', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка для политики конфиденциальности')),
                ('contract_offer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Договор оферты')),
                ('copyright', models.CharField(blank=True, max_length=100, null=True, verbose_name='Копирайт')),
                ('ymap', django_ymap.fields.YmapCoord(max_length=200, verbose_name='Карта')),
                ('id_ym', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Номер счетчика яндекс метрики')),
                ('title_seo', models.CharField(blank=True, max_length=255, null=True, verbose_name='title seo')),
                ('description_seo', models.CharField(blank=True, max_length=255, null=True, verbose_name='description seo')),
                ('block', models.ManyToManyField(blank=True, null=True, through='landing.BlockToLanding', to='landing.Block')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Brand', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Лендинг',
                'verbose_name_plural': 'Лендинг',
                'unique_together': {('brand', 'type_product')},
            },
        ),
        migrations.CreateModel(
            name='Gallery2ProductsCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='landing/catalog/', verbose_name='Изображение')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.ProductsCatalog', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Галерея продукта',
                'verbose_name_plural': 'Галерея продукта',
                'ordering': ['priority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Gallery2Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='landing/block/gallery/', verbose_name='Изображение')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.Block')),
                ('gruop_catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.Catalog', verbose_name='Группа каталога')),
            ],
            options={
                'verbose_name': 'Галерея для блока',
                'verbose_name_plural': 'Галерея для блока',
                'ordering': ['priority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Comments2Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Максимальное количество символов 1500', max_length=1500, null=True, verbose_name='Описание')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='landing/block/', verbose_name='Изображение')),
                ('svg', models.FileField(blank=True, null=True, upload_to='landing/block/svg/', validators=[apps.landing.models.svg_validator], verbose_name='SVG изображение')),
                ('priority', models.PositiveSmallIntegerField(default=0, verbose_name='Приоритет')),
                ('column_number', models.PositiveSmallIntegerField(choices=[(1, 'Первая колонка'), (2, 'Вторая колонка')], db_index=True, default=1, verbose_name='Номер колонки')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('post', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('company', models.CharField(blank=True, max_length=255, null=True, verbose_name='Компания')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Block', verbose_name='Блок')),
            ],
            options={
                'verbose_name': 'Комментарий для блока',
                'verbose_name_plural': 'Комментарии для блока',
                'ordering': ['priority', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ColumnToCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Catalog', verbose_name='Каталог')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.SpecificationProduct')),
            ],
            options={
                'verbose_name': 'Добавить столбец продуктов каталога',
                'verbose_name_plural': 'Добавление столбцов продуктов каталога',
                'ordering': ['position', 'id'],
            },
        ),
        migrations.CreateModel(
            name='CheckBoxForm2Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Block', verbose_name='Блок')),
            ],
            options={
                'verbose_name': 'Чекбокс формы',
                'verbose_name_plural': 'Чекбоксы формы',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='column_product',
            field=models.ManyToManyField(blank=True, null=True, through='landing.ColumnToCatalog', to='landing.SpecificationProduct'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='landing.ProductsCatalog', verbose_name='Продукт'),
        ),
        migrations.AddField(
            model_name='blocktolanding',
            name='landing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Landing'),
        ),
        migrations.AddField(
            model_name='block',
            name='catalog',
            field=models.ManyToManyField(blank=True, null=True, to='landing.Catalog', verbose_name='Каталог'),
        ),
    ]