# Generated by Django 4.2.5 on 2023-10-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0004_acessomedico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acessomedico',
            name='token',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
