from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.contrib.admin.widgets import AdminFileWidget
from django.db.models import Count, Sum, Avg

from patient_chart.models import *


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        from django.utils.safestring import mark_safe
        return mark_safe(u''.join(output))


class SnapshotAdmin(admin.TabularInline):
    model = Snapshot
    fields = ('description', 'image', 'created_at')
    max_num = 500
    min_num = 1
    extra = 0

    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


class CashWarrantAdmin(admin.TabularInline):
    model = CashWarrant
    fields = ('cash', 'description', 'created_at')
    max_num = 500
    min_num = 1
    extra = 0


# @admin.register(CashWarrant)
# class CashWarrantsAdmin(admin.ModelAdmin):
#     def get_changelist(self, request, **kwargs):
#         return TotalAveragesChangeList


@admin.register(PatientChart)
class PatientChartAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'created_at']
    inlines = [SnapshotAdmin, CashWarrantAdmin]
    fieldsets = (
        ("Пациент", {
            'fields': ("card_number", "fullname", "male", "date_of_birth")
        }),
    )

