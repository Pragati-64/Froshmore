# Generated by Django 3.2.2 on 2021-07-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0006_auto_20210518_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_username', models.CharField(default='', max_length=80)),
                ('amount_paid', models.IntegerField(default=0)),
                ('item_type', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=500)),
                ('product_name', models.CharField(max_length=500)),
                ('transaction_success', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='tiffinservice',
            name='tiffinservice_description',
            field=models.TextField(default='', max_length=500),
        ),
    ]
