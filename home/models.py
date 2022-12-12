from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable

from magazine.models import MagazineIssue, MagazineArticle


class HomePage(Page):
    intro = RichTextField(blank=True)
    #templates= "home/home_page.html"


    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        InlinePanel(
            "featured_podcasts",
            heading="Featured podcasts",
            help_text="Select one or more podcasts to feature on the home page",
        ),
        InlinePanel(
            "featured_blogs",
            heading="Featured blogs",
            help_text="Select one or more blogs to feature on the home page",
        ),

    ]





    subpage_types = [
        "community.CommunityPage",

        "events.EventsIndexPage",
        "blogs.BlogsIndexPage",
        "wagtailpod.PodIndexPage",
        "facets.FacetIndexPage",
        "wagtailpod.PodIndexPage",
        "forms.ContactFormPage",
        "library.LibraryIndexPage",
        "magazine.MagazineIndexPage",
        "memorials.MemorialIndexPage",


        "subscription.ManageSubscriptionPage",
        "subscription.SubscriptionIndexPage",
        "wf_pages.WfPage",
        "wf_pages.WfPageCollectionIndexPage",
    ]

    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        # pylint: disable=E501
        context["current_issue"] = (
            MagazineIssue.objects.live().order_by("-publication_date").first()
        )

        return context


class HomePageFeaturedPodcast(Orderable):
    home_page = ParentalKey(
        "home.HomePage",
        null=True,
        on_delete=models.CASCADE,
        related_name="featured_podcasts",
    )
    event = models.ForeignKey(
        "wagtailpod.PodcastPage",
        null=True,
        on_delete=models.CASCADE,
        related_name="+",
    )

    panels = [PageChooserPanel("event", "wagtailpod.PodcastPage",)]

class HomePageFeaturedBlog(Orderable):
    home_page = ParentalKey(
        "home.HomePage",
        null=True,
        on_delete=models.CASCADE,
        related_name="featured_blogs",
    )
    event = models.ForeignKey(
        "blogs.Blog",
        null=True,
        on_delete=models.CASCADE,
        related_name="+",
    )

    panels = [PageChooserPanel("event", "blogs.Blog")]
