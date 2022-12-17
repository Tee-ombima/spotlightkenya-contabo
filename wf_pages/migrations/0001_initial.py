# Generated by Django 4.0.8 on 2022-12-17 19:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import documents.blocks
import re
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='WfPageCollection',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WfPageCollectionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='WfPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('heading_level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'Level 2 (child of level 1)'), ('h3', 'Level 3 (child of level 2)'), ('h4', 'Level 4 (child of level 3)'), ('h5', 'Level 5 (child of level 4)'), ('h6', 'Level 6 (child of level 5)')], help_text='These different heading levels help to communicate the organization and hierarchy of the content on a page.')), ('heading_text', wagtail.blocks.CharBlock(help_text='The text to appear in the heading.')), ('target_slug', wagtail.blocks.CharBlock(help_text='Used to link to a specific location within this page. A slug should only contain letters, numbers, underscore (_), or hyphen (-).', required=False, validators=(django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid'),))), ('color', wagtail_color_panel.blocks.NativeColorBlock(required=False))])), ('rich_text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'superscript', 'strikethrough', 'blockquote'])), ('quote', wagtail.blocks.BlockQuoteBlock()), ('document', documents.blocks.DocumentEmbedBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('spacer', wagtail.blocks.StructBlock([('height', wagtail.blocks.DecimalBlock(decimal_places=1, help_text="The height of this spacer in 'em' values where 1 em is one uppercase M.", min_value=0))]))], use_json_field=True)),
                ('body_migrated', models.TextField(blank=True, help_text='Used only for content from old Drupal website.', null=True)),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages', to='wf_pages.wfpagecollection')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
