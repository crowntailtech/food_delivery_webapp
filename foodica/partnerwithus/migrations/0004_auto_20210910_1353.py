# Generated by Django 3.2.6 on 2021-09-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerwithus', '0003_auto_20210909_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner_with_us',
            name='aadhar_file',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='gst_file',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='img_file',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='menu_file',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='sign_file',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
    ]
