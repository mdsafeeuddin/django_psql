from django.contrib import admin

# Register your models here.
from .models import Section, Topic, Query

class SectionAdmin(admin.ModelAdmin):
  list_display = ('section_title', 'created')

class TopicAdmin(admin.ModelAdmin):
  list_display = ('topic', 'section', 'created')

class QueryAdmin(admin.ModelAdmin):
  list_display = ('query_text', 'topic', 'created')

admin.site.register(Section, SectionAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Query, QueryAdmin)