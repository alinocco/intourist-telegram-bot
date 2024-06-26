# Generated by Django 5.0.6 on 2024-06-25 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Гид',
                'verbose_name_plural': 'Гиды',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Долгота')),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=9, verbose_name='Широта')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('complexity', models.CharField(choices=[('light', 'Лёгкий'), ('medium', 'Средний'), ('hard', 'Сложный')], max_length=255, verbose_name='Сложность')),
                ('program', models.JSONField(blank=True, null=True, verbose_name='Программа')),
                ('schedule', models.JSONField(blank=True, null=True, verbose_name='Расписание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Расписание активировано')),
            ],
            options={
                'verbose_name': 'Тур',
                'verbose_name_plural': 'Туры',
            },
        ),
        migrations.CreateModel(
            name='TourInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='Дата')),
                ('status', models.CharField(choices=[('pending', 'Набор пока не открыт'), ('open', 'Набор открыт'), ('closed', 'Набор закрыт'), ('cancelled', 'Отменён')], max_length=255, verbose_name='Статус')),
                ('telegram_group', models.URLField(max_length=255, verbose_name='Telegram группа')),
                ('whatsapp_group', models.URLField(max_length=255, verbose_name='WhatsApp группа')),
                ('maximum_people', models.PositiveIntegerField(default=17, verbose_name='Максимум человек')),
                ('guides', models.ManyToManyField(related_name='tour_instances', to='tours.guide')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tour_instances', to='tours.tour')),
            ],
            options={
                'verbose_name': 'Отдельный тур',
                'verbose_name_plural': 'Отдельный туры',
            },
        ),
        migrations.CreateModel(
            name='TourLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Порядок')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.location')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tour')),
            ],
            options={
                'verbose_name': 'Локация туров',
                'verbose_name_plural': 'Локации туров',
            },
        ),
        migrations.AddField(
            model_name='tour',
            name='locations',
            field=models.ManyToManyField(related_name='tours', through='tours.TourLocation', to='tours.location'),
        ),
    ]
