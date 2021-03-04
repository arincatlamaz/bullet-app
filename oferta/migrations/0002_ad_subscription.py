

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oferta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.SmallIntegerField(choices=[(1, 'Driver'), (2, 'Passenger')], verbose_name='kind')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('departure', models.DateTimeField(verbose_name='Departue')),
                ('departure_postcode', models.CharField(max_length=5, verbose_name='departure postcode')),
                ('departure_street', models.CharField(max_length=500, verbose_name='departure street')),
                ('departure_home', models.CharField(max_length=50, verbose_name='departure home number')),
                ('arrival_code', models.CharField(max_length=5, verbose_name='arrival postcode')),
                ('arrival_street', models.CharField(max_length=500, verbose_name='arrival street')),
                ('arrival_home', models.CharField(max_length=50, verbose_name='arrival home number')),
                ('seats', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='Seats / peoples')),
                ('price', models.DecimalField(decimal_places=2, max_digits=13, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
                ('car_model', models.CharField(max_length=50, verbose_name='Car model')),

                ('completed', models.BooleanField(blank=True, default=False, verbose_name='comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Ad',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, 'Initial'), (2, 'Confirmed'), (2, 'Rejected')], verbose_name='Status')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oferta.ad', verbose_name='Ad')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
