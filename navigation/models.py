from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.core.fields import StreamField

from .blocks import (
    NavigationDropdownMenuBlock,
    NavigationExternalLinkBlock,
    NavigationPageChooserBlock,
)


@register_setting
class NavigationMenuSetting(BaseGenericSetting):
    items = StreamField(
        [
            ("internal_page", NavigationPageChooserBlock()),
            ("external_link", NavigationExternalLinkBlock()),
            ("drop_down", NavigationDropdownMenuBlock()),
        ]
        ,use_json_field=True,
    )

    panels = [
        FieldPanel("items"),
    ]

    class Meta:
        verbose_name = "Navigation menu"
