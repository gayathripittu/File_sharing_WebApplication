# Generated by Django 4.1.2 on 2022-11-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Enter first name')),
                ('email', models.EmailField(max_length=20, verbose_name='Enter Email')),
                ('password', models.CharField(max_length=80, verbose_name='Enter password')),
            ],
        ),
    ]
