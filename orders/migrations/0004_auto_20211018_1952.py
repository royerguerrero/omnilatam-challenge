# Generated by Django 3.2.8 on 2021-10-18 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20211018_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='productorder',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='shipping',
            old_name='modified_at',
            new_name='updated_at',
        ),
    ]
