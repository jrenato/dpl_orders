# DPL Orders

## VSCode setup

Add the following to settings.json

```
{
    "pylint.args": [
        "--load-plugins=pylint_django",
        "--django-settings-module=dpl_orders.settings",
    ],
}
```