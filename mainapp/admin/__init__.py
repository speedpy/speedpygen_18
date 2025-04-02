from django.contrib import admin
from mainapp.models import *

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'content']

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['pk']
    search_fields = ['content']

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['pk']

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(NoteLabel)
class NoteLabelAdmin(admin.ModelAdmin):
    list_display = ['pk']
