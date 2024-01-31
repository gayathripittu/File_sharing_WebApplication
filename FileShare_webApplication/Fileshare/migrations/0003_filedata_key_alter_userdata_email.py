# Generated by Django 4.1.2 on 2022-11-10 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fileshare', '0002_filedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='filedata',
            name='key',
            field=models.CharField(default='0000000', max_length=80, verbose_name='Enter key'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(max_length=40, verbose_name='Enter Email'),
        ),
    ]
