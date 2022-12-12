from django.db import models
from django.shortcuts import render
from django.utils import timezone

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.panels import FieldPanel
#from wagtail.images.panels import FieldPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag

#from wagtailmedia.panels import MediaChooserPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.admin.panels import FieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from streams.blocks import FormattedImageChooserStructBlock, HeadingBlock, SpacerBlock

# Podcast Site Pages

# Tags are not consistenetly sorted. Need way to sort tags.

class PodIndexPage(Page):

    subtitle = models.CharField(max_length=250, default="changeme")
    author = models.CharField(max_length=250, default="Dan and Luke")
    itunes_name = models.CharField(max_length=250, default="DCBC")
    author_email = models.CharField(max_length=250, default="dcbc@dontcallitabookclub.com")
    description = RichTextField(blank=False)
    itunes_categories = ["test"]
    categories = ["test"]
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True, #I think this solves the default image problem. Otherwise an image would have to be loaded with the site.
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        FieldPanel('itunes_name'),
        FieldPanel('author_email'),
        FieldPanel('description'),
        FieldPanel('image'),
    ]


    subpage_types = ['wagtailpod.PodcastPage']
    parent_page_types = ["home.HomePage"]




    max_count = 1


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        upcoming_podcasts = (
            PodcastPage.objects.all()

            .order_by("-date")
        )

        # Show three archive issues per page
        paginator = Paginator(upcoming_podcasts, 10)

        upcoming_podcasts_page = request.GET.get("page")

        tag = request.GET.get('tag')
        if tag:
            podcasts = podcasts.filter(tags__name=tag)

        try:
            paginated_podcasts = paginator.page(upcoming_podcasts_page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paginated_podcasts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            paginated_podcasts = paginator.page(paginator.num_pages)

        context["podcasts"] = paginated_podcasts

        return context

class PodcastPageTag(TaggedItemBase):
    content_object = ParentalKey('PodcastPage', on_delete=models.CASCADE, related_name='podcast_tags')


class PodcastPage(Page):
    date = models.DateTimeField("Post Date", default=timezone.now)
    description = RichTextField(blank=False)
    tags = ClusterTaggableManager(through=PodcastPageTag, blank=True)
    audio = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(
        [
            ("heading", HeadingBlock()),
            ("rich_text", blocks.RichTextBlock()),
            ("image", FormattedImageChooserStructBlock()),
            ("spacer", SpacerBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    sode_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('audio'),
        FieldPanel('tags'),
        FieldPanel('description'),
        FieldPanel("body"),
        FieldPanel('sode_image'),
    ]
    subpage_types = []

    parent_page_types = ['wagtailpod.PodIndexPage'] #May need to add home page. Don't know if inherits.

    def get_absolute_url(self):
        return self.get_url() #Should add request
