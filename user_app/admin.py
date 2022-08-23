from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MemberProfile, StaffProfile
from .forms import UserCreationForm, StaffCreationForm

class MemberAdmin(UserAdmin):
    ordering = ["id"]
    form = UserCreationForm
    model = MemberProfile
    list_display = ['username','email']

    fieldsets = (
        (None, {"fields": ("username","email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name","age","img")}),
        ("Important dates", {"fields": ("last_login","date_joined")})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide", ),
            "fields": ("username", "password1", "password2",\
                "img",'age','email','first_name','last_name')
        }),
    )


class StaffAdmin(UserAdmin):
    ordering = ["id"]
    form = StaffCreationForm
    model = StaffProfile
    list_display = ['username','email']
    
    fieldsets = (
        (None, {"fields": ("username","email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name","img")}),
        ("Important dates", {"fields": ("last_login","date_joined")})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide", ),
            "fields": ("username", "password1", "password2",\
                "img",'email','first_name','last_name')
        }),
    )


admin.site.register(MemberProfile, MemberAdmin)
admin.site.register(StaffProfile, StaffAdmin)