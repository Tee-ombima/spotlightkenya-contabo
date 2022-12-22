# Generated by Django 4.0.8 on 2022-12-22 08:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationMenuSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', wagtail.fields.StreamField([('internal_page', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('anchor', wagtail.blocks.CharBlock(help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.", required=False))])), ('external_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock()), ('anchor', wagtail.blocks.CharBlock(help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.", required=False))])), ('drop_down', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('items', wagtail.blocks.StreamBlock([('page', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('page', wagtail.blocks.PageChooserBlock()), ('anchor', wagtail.blocks.CharBlock(help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.", required=False))])), ('external_link', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock()), ('anchor', wagtail.blocks.CharBlock(help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.", required=False))]))]))]))], use_json_field=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Navigation menu',
            },
        ),
    ]
