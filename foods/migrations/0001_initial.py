# Generated by Django 4.0.4 on 2022-04-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام ')),
                ('descriptions', models.CharField(max_length=255, verbose_name='توضیحات ')),
                ('price', models.IntegerField(default=0, verbose_name='قیمت ')),
                ('photo', models.ImageField(upload_to='image/', verbose_name='تصویر ')),
            ],
        ),
    ]
