# Generated by Django 5.0.6 on 2024-05-17 06:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recommand", "0002_remove_upload_image_컬럼_업로드날짜_upload_image_title_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="upload_image",
            name="title",
        ),
    ]