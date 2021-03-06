# Generated by Django 3.1.6 on 2021-02-16 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload_data', '0004_auto_20210216_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='Event_Name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='participantdata',
            name='Event_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='eventsname', to='upload_data.certificate'),
        ),
    ]
