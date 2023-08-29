# Generated by Django 3.2.6 on 2021-09-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerwithus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FSSAI_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fssai_num', models.IntegerField()),
                ('fssai_exp_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GSTPAN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_num', models.IntegerField()),
                ('pan_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='own_bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_num', models.IntegerField()),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Owner_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('own_name', models.CharField(max_length=50)),
                ('own_aadhar', models.IntegerField()),
                ('own_file', models.FileField(null=True, upload_to='files/', verbose_name='')),
                ('own_address', models.CharField(max_length=250)),
                ('own_mobile', models.IntegerField()),
            ],
        ),
    ]
