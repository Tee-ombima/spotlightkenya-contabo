from datetime import date

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.db.models import Q

from timezone_field import TimeZoneField
from wagtail.admin.panels import FieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.search import index

from streams.blocks import FormattedImageChooserStructBlock, HeadingBlock, SpacerBlock
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation



class Blog(Page, HitCountMixin):
    teaser = models.TextField(max_length=100, null=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

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

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    timezone = TimeZoneField(
        default="Africa/Nairobi",
        choices_display="WITH_GMT_OFFSET",
    )

    website = models.URLField(blank=True, null=True, max_length=300)

    drupal_node_id = models.IntegerField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("teaser"),
        FieldPanel("body"),
        FieldPanel("start_date"),
        FieldPanel("end_date"),
        FieldPanel("timezone"),
        FieldPanel("website"),
    ]

    context_object_name = "blog"

    search_template = "search/blog.html"

    search_fields = Page.search_fields + [
        index.SearchField("body", partial_match=True),
    ]

    parent_page_types = ["blogs.BlogsIndexPage"]
    subpage_types = []

    class Meta:
        db_table = "blogs"
        ordering = ["start_date"]


class BlogsIndexPage(Page):
    intro = RichTextField(blank=True)
    #templates = "blogs/blogs_index_page.html"

    content_panels = Page.content_panels + [FieldPanel("intro")]

    parent_page_types = ["home.HomePage"]
    subpage_types = ["blogs.Blog"]

    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        upcoming_blogs = (
            Blog.objects.all()

            .order_by("-start_date")
        )

        # Show three archive issues per page
        paginator = Paginator(upcoming_blogs, 7)

        upcoming_blogs_page = request.GET.get("page")

        try:
            paginated_blogs = paginator.page(upcoming_blogs_page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paginated_blogs = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            paginated_blogs = paginator.page(paginator.num_pages)

        context["blogs"] = paginated_blogs

        return context
