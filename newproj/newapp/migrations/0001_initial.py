# Generated by Django 4.2.4 on 2023-09-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myresume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('post', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('image', models.ImageField(null=True, upload_to='media')),
                ('linked_in', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('interest', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=500)),
                ('experience', models.CharField(max_length=400)),
            ],
        ),
    ]