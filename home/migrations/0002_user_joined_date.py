# Generated by Django 5.0.4 on 2024-04-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
