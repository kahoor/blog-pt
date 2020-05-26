from django.contrib import admin

from .models import MeasurableThing, Records, Kind
# Register your models here.

class RecordsInline(admin.TabularInline):
    '''Tabular Inline View for Records'''

    model = Records
    # min_num = 3
    # max_num = 20
    # extra = 1
    # raw_id_fields = (,)

@admin.register(MeasurableThing)
class MeasurableThingAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'user', 'started', 'record_display','kind']
    inlines = [RecordsInline]
    
    def record_display(self, obj):
        return Records.objects.filter(measurable_thing=obj).order_by('-created')[0]
    record_display.short_description = 'last_record'

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ['scale']