from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from django.forms.widgets import SelectMultiple
from rest_framework.authtoken.models import TokenProxy

from account.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'15', 'style': 'color:blue; width:250px'})},
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'15', 'style': 'color:blue; height: 50px'})},
    }
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'is_staff', 'is_superuser', 'last_login', 'groups')
        }),
    )

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


class GroupsAdmin(admin.ModelAdmin):
    list_display = ["name"]

    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size': '15', 'style': 'color:blue; width:350px'})},
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size': '15', 'style': 'color:blue; height: 650px'})},
    }

    class Meta:
        model = Group


admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
admin.site.register(Group, GroupsAdmin)