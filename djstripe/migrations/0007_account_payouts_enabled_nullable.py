# Generated by Django 3.0.5 on 2020-05-03 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0006_2_3"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="payouts_enabled",
            field=models.BooleanField(
                help_text="Whether Stripe can send payouts to this account", null=True
            ),
        ),
    ]
