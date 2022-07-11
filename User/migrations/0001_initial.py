# Generated by Django 4.0.5 on 2022-07-11 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Currencies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('currency', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Currencies.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('health', models.IntegerField(default=100)),
                ('strength_n', models.IntegerField(default=0)),
                ('strength', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('militaryrank', models.IntegerField(default=0)),
                ('productivity', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('fairness', models.IntegerField(default=0)),
                ('political_achievement', models.IntegerField(default=0)),
                ('xp', models.IntegerField(default=0)),
                ('bio', models.TextField(max_length=200)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
                ('friends', models.ManyToManyField(blank=True, to='User.profile')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_location', to='Location.region')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Location.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.profile')),
            ],
        ),
        migrations.CreateModel(
            name='CountryBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.country')),
                ('currency', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Currencies.currency')),
            ],
        ),
    ]
