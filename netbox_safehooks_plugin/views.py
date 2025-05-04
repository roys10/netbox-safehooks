from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class SafeHooksView(generic.ObjectView):
    queryset = models.SafeHooks.objects.all()


class SafeHooksListView(generic.ObjectListView):
    queryset = models.SafeHooks.objects.all()
    table = tables.SafeHooksTable


class SafeHooksEditView(generic.ObjectEditView):
    queryset = models.SafeHooks.objects.all()
    form = forms.SafeHooksForm


class SafeHooksDeleteView(generic.ObjectDeleteView):
    queryset = models.SafeHooks.objects.all()
