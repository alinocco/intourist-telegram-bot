# Generated by Django 5.0.6 on 2024-06-28 16:12

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_alter_guide_created_date_alter_guide_modified_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tourinstance',
            options={'verbose_name': 'Отдельный тур', 'verbose_name_plural': 'Отдельные туры'},
        ),
        migrations.AlterField(
            model_name='tour',
            name='schedule',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=13, null=True, verbose_name='Расписание создания'),
        ),
        migrations.AlterField(
            model_name='tourinstance',
            name='status',
            field=models.CharField(choices=[('pending', 'Набор пока не открыт'), ('open', 'Набор открыт'), ('closed', 'Набор закрыт'), ('cancelled', 'Отменён')], default='pending', max_length=255, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='tourinstance',
            name='telegram_group',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Telegram группа'),
        ),
        migrations.AlterField(
            model_name='tourinstance',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tour_instances', to='tours.tour', verbose_name='Тур'),
        ),
        migrations.AlterField(
            model_name='tourinstance',
            name='whatsapp_group',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='WhatsApp группа'),
        ),
    ]
