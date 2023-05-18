# Generated by Django 4.2.1 on 2023-05-04 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_room_room_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='room',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.AddField(
            model_name='payment',
            name='reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='reservation.reservation'),
        ),
    ]