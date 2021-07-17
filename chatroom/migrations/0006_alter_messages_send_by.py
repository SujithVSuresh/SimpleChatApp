# Generated by Django 3.2.2 on 2021-07-14 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatroom', '0005_messages_send_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='send_by',
            field=models.ForeignKey(default='request.user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
