# Generated by Django 4.2.1 on 2023-05-13 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_alter_payment_amount_alter_payment_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='reservation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='reservation.reservation', verbose_name='reservations'),
        ),
    ]