from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from blogs.models import Blog
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from wagtail import hooks



@hooks.register("before_serve_page")
def increment_view_count(page, request, serve_args, serve_kwargs):
    if page.specific_class == Blog:
        hit_count = HitCount.objects.get_for_object(page)
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        #Blog.objects.filter(pk=page.pk).update(view_count=F('view_count') + 1)

class BlogModelAdmin(ModelAdmin):
    model = Blog
    menu_icon = "date"
    menu_label = "Blogs"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_per_page = 10
    ordering = ["start_date"]
    list_display = (
        "title",
        "start_date",
        "end_date",
        "live",
    )
    empty_value_display = "-"
    search_fields = ("title", "description")
    list_filter = ("start_date",)


modeladmin_register(BlogModelAdmin)
