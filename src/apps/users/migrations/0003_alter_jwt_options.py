# Generated by Django 5.0.6 on 2024-05-23 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_searcheruser_address_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jwt",
            options={"verbose_name": "JWT", "verbose_name_plural": "JWT's"},
        ),
    ]
