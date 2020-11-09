from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from promo.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + tuple(
        auth_admin.UserAdmin.fieldsets
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
    fieldsets = (
        (
            None,
            {"fields": ("name", "address", "mobile_number", "type")},
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups")},
        ),
    )

    def has_module_permission(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

    def has_view_permission(self, request, obj=None):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
