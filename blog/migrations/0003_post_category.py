# Generated by Django 3.2.5 on 2021-07-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210717_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.Categoty', verbose_name='دسته بندی'),
        ),
    ]
