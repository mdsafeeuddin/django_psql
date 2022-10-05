from django.contrib import admin

# Register your models here.
from .models import Section
from .models import Topic

admin.site.register(Section)
admin.site.register(Topic)