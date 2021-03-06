# Generated by Django 4.0.5 on 2022-07-11 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
                ('sales_tax', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('income_tax', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('import_tax', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('trade_license_fees', models.IntegerField(default=0)),
                ('minimum_wage', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('gold_amount', models.IntegerField(default=0)),
                ('Currency_amount', models.IntegerField(default=10)),
                ('government_type', models.CharField(choices=[('DE', 'Democracy'), ('DD', 'Direct democracy'), ('DC', 'Dictatorship')], max_length=100)),
                ('free_trade_agreements', models.ManyToManyField(to='Location.country')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
                ('country', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='region_set', to='Location.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fortification', models.CharField(choices=[('BW', 'Basic Wall'), ('FW', 'Fortified Wall')], max_length=2)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.region')),
            ],
        ),
    ]
