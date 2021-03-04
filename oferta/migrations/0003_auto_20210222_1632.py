

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oferta', '0002_ad_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='arrival_code',
            new_name='arrival_postcode',
        ),
    ]
