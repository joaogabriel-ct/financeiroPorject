# Generated by Django 5.0.1 on 2024-03-19 02:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("controle", "0004_transacao_total_parcelas"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transacao",
            name="total_parcelas",
        ),
    ]
