from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
# from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.admin.panels import MultiFieldPanel, FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("body", classname="full") ]
