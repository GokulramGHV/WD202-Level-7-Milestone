# Generated by Django 4.0.1 on 2022-02-18 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_status', models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=50)),
                ('updated_status', models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED'), ('CANCELLED', 'CANCELLED')], default='PENDING', max_length=50)),
                ('changed_date', models.DateField(auto_now=True)),
                ('task_changed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
