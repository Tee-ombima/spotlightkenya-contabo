from wagtail import hooks
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from wagtail.core.models import PageViewRestriction

@hooks.register('before_serve_page')
def check_view_restrictions(page, request, serve_args, serve_kwargs):
    """
    Overriding wagtail check_view_restrictions to redirect a user to the dashboard
    when they are logged in and the page has groups restriction_type.
    The dashboard serve view is handling the permission denied modal
    """
    for restriction in page.get_view_restrictions():
      if not restriction.accept_request(request):
        if restriction.restriction_type == PageViewRestriction.PASSWORD:
          from wagtail.core.forms import PasswordViewRestrictionForm
          form = PasswordViewRestrictionForm(instance=restriction,
                                              initial={'return_url': request.get_full_path()})
          action_url = reverse('wagtailcore_authenticate_with_password', args=[
                                restriction.id, page.id])
          return page.serve_password_required_response(request, form, action_url)

        elif request.user.is_authenticated and restriction.restriction_type == PageViewRestriction.GROUPS:

          return redirect("https://www.spotlightkenya.club/payment-confirmation/")
