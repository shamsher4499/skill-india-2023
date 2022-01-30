# Generated by Django 3.0.8 on 2021-08-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210625_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additiondetail',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='additiondetail',
            name='district',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='additiondetail',
            name='indent_mark',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='additiondetail',
            name='other_contact',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='additiondetail',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='additiondetail',
            name='pin_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]