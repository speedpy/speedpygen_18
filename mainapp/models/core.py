from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
class Note(models.Model):
    title = models.CharField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_notes")
    def __str__(self):
        return str(self.title)

class Conversation(models.Model):
    name = models.CharField(blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_conversations")
    def __str__(self):
        return str(self.name)

class Message(models.Model):
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False, null=False)
    conversation = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Conversation", related_name="conversation_messages")
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_messages")
    def __str__(self):
        return str(self.id)

class Attachment(models.Model):
    file = models.FileField(blank=False, null=False, upload_to="file_uploads/")
    message = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Message", related_name="message_attachments")
    def __str__(self):
        return str(self.id)

class Label(models.Model):
    name = models.CharField(blank=False, null=False, unique=True)
    user = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to=User, related_name="user_labels")
    def __str__(self):
        return str(self.name)

class NoteLabel(models.Model):
    note = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Note", related_name="note_notelabels")
    label = models.ForeignKey(blank=False, null=False, on_delete=models.CASCADE, to="mainapp.Label", related_name="label_notelabels")
    def __str__(self):
        return str(self.id)
