import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("token_blacklist", "0012_alter_outstandingtoken_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name='outstandingtoken',
            name='jti',
            field=models.CharField(unique=True, max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='outstandingtoken',
            name='expires_at',
            field=models.DateTimeField(db_index=True)
        ),
        migrations.AlterField(
            model_name='blacklistedtoken',
            name='blacklisted_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True)
        ),
    ]
    
