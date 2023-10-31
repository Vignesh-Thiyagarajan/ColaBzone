from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..ColabUsers.models import ColabUser
from .forms import ColabUserCreationForm, ColabUserChangeForm


class ColabUserAdmin(UserAdmin):
    add_form = ColabUserCreationForm
    form = ColabUserChangeForm
    model = ColabUser

    def user_type(self, obj):
        return obj.user_type.user_type

    list_display = ('email', 'user_type', 'is_active')
    list_filter = ('is_active', 'user_type')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'user_type', 'groups')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
    )

    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)


# Register your custom user admin
admin.site.register(ColabUser, ColabUserAdmin)
