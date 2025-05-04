from netbox.filtersets import NetBoxModelFilterSet
from .models import SafeHooks


# class SafeHooksFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = SafeHooks
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
