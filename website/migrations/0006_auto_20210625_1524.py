# Generated by Django 3.1.7 on 2021-06-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210625_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestnotification',
            name='double_payment_status',
            field=models.CharField(blank=True, default='Active', max_length=254, null=True),
        ),
    ]