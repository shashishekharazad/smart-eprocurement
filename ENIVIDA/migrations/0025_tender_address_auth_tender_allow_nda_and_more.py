# Generated by Django 4.1 on 2022-08-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0024_remove_user_bidder_email_remove_user_bidder_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='Address_Auth',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Allow_NDA',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Allow_Preferential',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Bid_Submission_End_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Bid_Submission_Start_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Bid_Validity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tender',
            name='Clarification_End_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Clarification_Start_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Contract_Type',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='EMD_Amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tender',
            name='EMD_Exemption_Allowed',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='EMD_Fee_Type',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='EMD_Payable_At',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='EMD_Payable_To',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='EMD_Percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tender',
            name='Fee_Payable_At',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Fee_Payable_To',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Location',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Meeting_Address',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Meeting_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Meeting_Place',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='NDA',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Name_Auth',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Opening_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Opening_Place',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Organisation_chain',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Period_Of_Work',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tender',
            name='Pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tender',
            name='Product_Category',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Published_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Sale_Start_Date',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Sub_category',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Tender_Fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tender',
            name='Tender_Fee_Exemption_Allowed',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Tender_Value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tender',
            name='Title',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='tender',
            name='Work_Description',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
