# Generated by Django 4.2.4 on 2023-09-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_remove_resume_interest_2_remove_resume_interest_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='percent_1',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='resume',
            name='percentage_1',
            field=models.CharField(max_length=70),
        ),
    ]
