# Generated by Django 3.2.2 on 2021-07-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='value',
            field=models.CharField(max_length=200),
        ),
    ]