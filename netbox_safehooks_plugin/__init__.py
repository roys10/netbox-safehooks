"""Top-level package for NetBox SafeHooks Plugin."""

__author__ = """Roy M. Segev"""
__email__ = ""
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class SafeHooksConfig(PluginConfig):
    name = "netbox_safehooks_plugin"
    verbose_name = "NetBox SafeHooks Plugin"
    description = "NetBox plugin for monitoring and rolling back webhooks"
    version = "version"
    base_url = "netbox_safehooks_plugin"


config = SafeHooksConfig
