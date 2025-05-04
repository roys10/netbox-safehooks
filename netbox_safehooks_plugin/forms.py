from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import SafeHooks


class SafeHooksForm(NetBoxModelForm):
    class Meta:
        model = SafeHooks
        fields = ("name", "tags")
