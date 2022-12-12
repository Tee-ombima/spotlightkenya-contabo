# Generated by Django 4.0.8 on 2022-10-16 08:43

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_alter_magazinearticle_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazineissue',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], default='', use_json_field=True),
        ),
    ]
