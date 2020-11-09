from django.contrib import admin

# ----------------------My App Models----------------------
from .models import Promo


class PromoAdmin(admin.ModelAdmin):
    fields = [
        "promo_type",
        "promo_code",
        "creation_time",
        "start_time",
        "end_time",
        "promo_amount",
        "is_active",
        "description",
        "user",
    ]
    list_display = ["id", "promo_code", "is_active"]
    readonly_fields = [
        "creation_time",
    ]


# Register the admin class with the associated model
admin.site.register(Promo, PromoAdmin)