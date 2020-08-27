from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Novel)
admin.site.register(Comment)

class NovelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ','.join(o.name for o in obj.tags.all())