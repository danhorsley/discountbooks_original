# Generated by Django 3.2.6 on 2021-08-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappia', '0005_alter_bookdata_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='isbn10',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='isbn13',
            field=models.CharField(max_length=20),
        ),
    ]
