from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("safehookss/", views.SafeHooksListView.as_view(), name="safehooks_list"),
    path("safehookss/add/", views.SafeHooksEditView.as_view(), name="safehooks_add"),
    path("safehookss/<int:pk>/", views.SafeHooksView.as_view(), name="safehooks"),
    path("safehookss/<int:pk>/edit/", views.SafeHooksEditView.as_view(), name="safehooks_edit"),
    path("safehookss/<int:pk>/delete/", views.SafeHooksDeleteView.as_view(), name="safehooks_delete"),
    path(
        "safehookss/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="safehooks_changelog",
        kwargs={"model": models.SafeHooks},
    ),
)
