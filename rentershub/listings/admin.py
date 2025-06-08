from django.contrib import admin
from .models import PropertyPost, PropertyImages


@admin.register(PropertyPost)
class PropertyPostAdmin(admin.ModelAdmin):
    pass

@admin.register(PropertyImages)
class PropertyImagesAdmin(admin.ModelAdmin):
    pass
