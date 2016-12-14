from django.conf.urls import url

from checker.views import SiteFormView

urlpatterns = [
    url(
        regex=r"create$",
        view=SiteFormView.as_view(),
        name="create"
    )
]
