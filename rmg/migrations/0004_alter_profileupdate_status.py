# Generated by Django 5.1.7 on 2025-03-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmg', '0003_profileupdate_marked_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileupdate',
            name='status',
            field=models.CharField(choices=[('CV Shared', 'CV Shared'), ('CV Rejected', 'CV Rejected'), ('Awaiting L1', 'Awaiting L1'), ('L1 Rejected', 'L1 Rejected'), ('Awaiting L2', 'Awaiting L2'), ('L2 Rejected', 'L2 Rejected'), ('Awaiting L3', 'Awaiting L3'), ('L3 Rejected', 'L3 Rejected'), ('Awaiting Feedback', 'Awaiting Feedback'), ('Awaiting Kickstart', 'Awaiting Kickstart'), ('Fulfilled', 'Fulfilled'), ('Inactivated', 'Inactivated')], default='CV Shared', max_length=50),
        ),
    ]
