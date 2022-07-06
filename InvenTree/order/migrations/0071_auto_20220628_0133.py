# Generated by Django 3.2.13 on 2022-06-28 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0077_alter_stockitem_notes'),
        ('part', '0079_alter_part_notes'),
        ('order', '0070_auto_20220620_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorderallocation',
            name='item',
            field=models.ForeignKey(help_text='Select stock item to allocate', limit_choices_to={'belongs_to': None, 'part__salable': True, 'part__virtual': False, 'sales_order': None}, on_delete=django.db.models.deletion.CASCADE, related_name='sales_order_allocations', to='stock.stockitem', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='salesorderlineitem',
            name='part',
            field=models.ForeignKey(help_text='Part', limit_choices_to={'salable': True, 'virtual': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales_order_line_items', to='part.part', verbose_name='Part'),
        ),
    ]