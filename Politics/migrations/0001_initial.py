# Generated by Django 4.0.5 on 2022-07-09 06:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Location', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupremeCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.profile')),
            ],
        ),
        migrations.CreateModel(
            name='NationalPolicies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_tax', models.DecimalField(decimal_places=2, default=1, max_digits=4, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('sales_tax', models.DecimalField(decimal_places=2, default=1, max_digits=4, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('import_tax', models.DecimalField(decimal_places=2, default=1, max_digits=4, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('trade_license_fees', models.IntegerField(default=0)),
                ('minimum_wage', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('government_type', models.CharField(choices=[('DE', 'democracy'), ('DD', 'direct democracy'), ('DC', 'dictatorship')], max_length=100)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='national_policies', to='Location.country')),
                ('free_trade_agreements', models.ManyToManyField(to='Location.country')),
            ],
        ),
        migrations.CreateModel(
            name='Mayor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declaration_date', models.DateTimeField(auto_now_add=True)),
                ('country_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
                ('country_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enemy_country', to='Location.country')),
            ],
        ),
        migrations.CreateModel(
            name='Embargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='embargoed_country', to='Location.country')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
            ],
        ),
        migrations.CreateModel(
            name='CountryPresident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
                ('president', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Ally',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declaration_date', models.DateTimeField(auto_now_add=True)),
                ('country_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
                ('country_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allied_country', to='Location.country')),
            ],
        ),
        migrations.AddConstraint(
            model_name='enemy',
            constraint=models.UniqueConstraint(fields=('country_1', 'country_2', 'declaration_date'), name='unique_enemies'),
        ),
        migrations.AddConstraint(
            model_name='embargos',
            constraint=models.UniqueConstraint(fields=('sender', 'receiver', 'date'), name='unique_embargo'),
        ),
        migrations.AlterUniqueTogether(
            name='countrypresident',
            unique_together={('country', 'president')},
        ),
        migrations.AddConstraint(
            model_name='ally',
            constraint=models.UniqueConstraint(fields=('country_1', 'country_2', 'declaration_date'), name='unique_allies'),
        ),
    ]