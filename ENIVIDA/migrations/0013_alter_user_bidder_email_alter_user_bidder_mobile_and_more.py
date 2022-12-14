# Generated by Django 4.1 on 2022-08-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0012_alter_user_bidder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Bidder_Email',
            field=models.EmailField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='Bidder_Mobile',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='City',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='Company_Name',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='Deignation',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='Legel_Status',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='Nature_of_Business',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='PAN_TAN_Number',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='Partners_or_Directors',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='Registered_Address',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='Registration_Number',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='State',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Gender',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Mobile',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Name',
            field=models.CharField(default=0, max_length=500),
        ),
    ]
