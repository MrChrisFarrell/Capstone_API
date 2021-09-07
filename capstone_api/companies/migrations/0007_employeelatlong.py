# Generated by Django 3.2.5 on 2021-09-07 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_alter_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLatLong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.employee')),
            ],
        ),
    ]
