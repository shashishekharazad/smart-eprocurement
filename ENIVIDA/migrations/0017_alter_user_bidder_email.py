# Generated by Django 4.1 on 2022-08-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0016_alter_user_bidder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Bidder_Email',
            field=models.EmailField(max_length=25, null=True),
        ),
    ]
