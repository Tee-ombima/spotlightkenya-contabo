from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from blogs.models import Blog
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.core.exceptions import PermissionDenied
from django.views.defaults import permission_denied
from wagtail import hooks


@hooks.register('construct_explorer_page_queryset')
def show_authors_only_their_articles(parent_page, pages, request):
    user_group = request.user.groups.filter(name='Author').exists()
    if user_group:
        pages = pages.filter(owner=request.user)

    return pages

@hooks.register('before_edit_page')
def before_edit_page(request, page):
    # user_group = request.user.groups.filter(name='Author').exists() # I did not use user_group
    if not (request.user.is_superuser or page.owner == request.user):
        return permission_denied(request, PermissionDenied("You do not have permission to edit this page."))

@hooks.register('before_delete_page')
def before_delete_page(request, page):
    if not (request.user.is_superuser or page.owner == request.user):
        return permission_denied(request,PermissionDenied("You do not have permission to delete this page."))

@hooks.register('before_create_page')
def before_create_page(request, parent_page, page_class):
    if not (request.user.is_superuser or page_class == Article):
        return permission_denied(request, PermissionDenied("You do not have permission to add this page."))

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
        "owner"
    )
    empty_value_display = "-"
    search_fields = ("title", "owner")
    list_filter = ("start_date",)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        #only show articles from the current user
        return qs.filter(owner=request.user)


modeladmin_register(BlogModelAdmin)
