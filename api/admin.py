from django.apps import apps
from django.contrib import admin


class CustomAdmin(admin.ModelAdmin):
    readonly_fields = ['pkey']


apps = apps.get_app_config('api')
for model_name, model in apps.models.items():
    admin.site.register(model, CustomAdmin)
