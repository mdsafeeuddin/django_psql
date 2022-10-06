from django.contrib import admin

# Register your models here.
from .models import Section, Topic, Query

class TopicAdmin(admin.ModelAdmin):
  list_display = ('topic', 'section')

class QueryAdmin(admin.ModelAdmin):
  list_display = ('query_text', 'topic')

admin.site.register(Section)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Query, QueryAdmin)