# Generated by Django 4.2.1 on 2023-06-26 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_bill_amount_remove_bill_id_car_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_detail',
            name='id_bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.bill'),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='id_work_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.work_order'),
        ),
        migrations.AlterField(
            model_name='quotation_detail',
            name='id_quotation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.quotation'),
        ),
    ]
