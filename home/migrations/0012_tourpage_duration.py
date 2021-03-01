# Generated by Django 3.0.11 on 2021-03-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_tourpage_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpage',
            name='duration',
            field=models.CharField(blank=True, help_text='The duration. eg: 2 days', max_length=140),
        ),
    ]
