# Generated by Django 3.2.6 on 2021-09-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappia', '0009_auto_20210913_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('isbn10', models.CharField(max_length=20)),
                ('itemname', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('fulfilment', models.CharField(max_length=20)),
                ('productsales', models.FloatField(default=0)),
                ('postagecredits', models.FloatField(default=0)),
                ('sellingfees', models.FloatField(default=0)),
                ('fbspfees', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('isbn13', models.CharField(max_length=20)),
                ('cost', models.FloatField(default=0)),
                ('net_profit', models.FloatField(default=0)),
            ],
        ),
    ]
