# Generated by Django 3.2.2 on 2021-07-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0009_alter_hostel_hostel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='hostel_ac',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_area',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_contactnumber',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_deposit',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_mealtype',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_mess',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_pincode',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_rent',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_roomcleaning',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_state',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_vistorentry',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_watercooler',
            field=models.IntegerField(default=''),
        ),
    ]