from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_safehooks_plugin:safehooks_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_safehooks_plugin:safehooks_list",
        link_text="SafeHooks",
        buttons=plugin_buttons,
    ),
)
