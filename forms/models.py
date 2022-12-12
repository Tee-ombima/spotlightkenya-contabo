from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from modelcluster.fields import ParentalKey


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactFormPage", on_delete=models.CASCADE, related_name="form_fields"
    )


class ContactFormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    max_count = 1

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro", classname="full"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text", classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),

    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    def get_form_fields(self):
        return self.form_fields.all()
