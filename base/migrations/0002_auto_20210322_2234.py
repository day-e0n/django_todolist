# Generated by Django 3.1.7 on 2021-03-22 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]