# Generated by Django 4.0.8 on 2022-12-22 08:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re
import timezone_field.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('teaser', models.TextField(blank=True, max_length=100, null=True)),
                ('body', wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading_level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'Level 2 (child of level 1)'), ('h3', 'Level 3 (child of level 2)'), ('h4', 'Level 4 (child of level 3)'), ('h5', 'Level 5 (child of level 4)'), ('h6', 'Level 6 (child of level 5)')], help_text='These different heading levels help to communicate the organization and hierarchy of the content on a page.')), ('heading_text', wagtail.blocks.CharBlock(help_text='The text to appear in the heading.')), ('target_slug', wagtail.blocks.CharBlock(help_text='Used to link to a specific location within this page. A slug should only contain letters, numbers, underscore (_), or hyphen (-).', required=False, validators=(django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid'),))), ('color', wagtail_color_panel.blocks.NativeColorBlock(required=False))])), ('rich_text', wagtail.blocks.RichTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('width', wagtail.blocks.IntegerBlock(help_text='Enter the desired image width value in pixels up to 800 max.', max_value=800, min_value=0))])), ('spacer', wagtail.blocks.StructBlock([('height', wagtail.blocks.DecimalBlock(decimal_places=1, help_text="The height of this spacer in 'em' values where 1 em is one uppercase M.", min_value=0))]))], blank=True, null=True, use_json_field=True)),
                ('body2', wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading_level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'Level 2 (child of level 1)'), ('h3', 'Level 3 (child of level 2)'), ('h4', 'Level 4 (child of level 3)'), ('h5', 'Level 5 (child of level 4)'), ('h6', 'Level 6 (child of level 5)')], help_text='These different heading levels help to communicate the organization and hierarchy of the content on a page.')), ('heading_text', wagtail.blocks.CharBlock(help_text='The text to appear in the heading.')), ('target_slug', wagtail.blocks.CharBlock(help_text='Used to link to a specific location within this page. A slug should only contain letters, numbers, underscore (_), or hyphen (-).', required=False, validators=(django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid'),))), ('color', wagtail_color_panel.blocks.NativeColorBlock(required=False))])), ('rich_text', wagtail.blocks.RichTextBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('width', wagtail.blocks.IntegerBlock(help_text='Enter the desired image width value in pixels up to 800 max.', max_value=800, min_value=0))])), ('spacer', wagtail.blocks.StructBlock([('height', wagtail.blocks.DecimalBlock(decimal_places=1, help_text="The height of this spacer in 'em' values where 1 em is one uppercase M.", min_value=0))]))], blank=True, null=True, use_json_field=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('timezone', timezone_field.fields.TimeZoneField(choices_display='WITH_GMT_OFFSET', default='Africa/Nairobi')),
                ('website', models.URLField(blank=True, max_length=300, null=True)),
                ('drupal_node_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events',
                'ordering': ['start_date'],
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
