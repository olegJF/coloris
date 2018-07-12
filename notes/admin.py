from django.contrib import admin
from .models import *

class NoteAdmin(admin.ModelAdmin):
    exclude = ('unique_words',)


admin.site.register(Note, NoteAdmin)