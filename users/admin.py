from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # list_display = ['email', 'username', 'age']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
