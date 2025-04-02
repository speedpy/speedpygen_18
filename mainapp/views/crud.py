from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from mainapp.models import *
from django import forms

class NoteListView(ListView):
    model = Note
    template_name = 'mainapp/note_list.html'
    context_object_name = 'note_list'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'mainapp/note_detail.html'
    context_object_name = 'note'

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content', 'created_at', 'updated_at', 'user']

    template_name = 'mainapp/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content', 'created_at', 'updated_at', 'user']

    template_name = 'mainapp/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'mainapp/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

class ConversationListView(ListView):
    model = Conversation
    template_name = 'mainapp/conversation_list.html'
    context_object_name = 'conversation_list'

class ConversationDetailView(DetailView):
    model = Conversation
    template_name = 'mainapp/conversation_detail.html'
    context_object_name = 'conversation'

class ConversationCreateView(CreateView):
    model = Conversation
    fields = ['name', 'created_at', 'updated_at', 'user']

    template_name = 'mainapp/conversation_form.html'
    success_url = reverse_lazy('conversation_list')

class ConversationUpdateView(UpdateView):
    model = Conversation
    fields = ['name', 'created_at', 'updated_at', 'user']

    template_name = 'mainapp/conversation_form.html'
    success_url = reverse_lazy('conversation_list')

class ConversationDeleteView(DeleteView):
    model = Conversation
    template_name = 'mainapp/conversation_confirm_delete.html'
    success_url = reverse_lazy('conversation_list')

class MessageListView(ListView):
    model = Message
    template_name = 'mainapp/message_list.html'
    context_object_name = 'message_list'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'mainapp/message_detail.html'
    context_object_name = 'message'

class MessageCreateView(CreateView):
    model = Message
    fields = ['content', 'created_at', 'conversation', 'user']

    template_name = 'mainapp/message_form.html'
    success_url = reverse_lazy('message_list')

class MessageUpdateView(UpdateView):
    model = Message
    fields = ['content', 'created_at', 'conversation', 'user']

    template_name = 'mainapp/message_form.html'
    success_url = reverse_lazy('message_list')

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mainapp/message_confirm_delete.html'
    success_url = reverse_lazy('message_list')

class AttachmentListView(ListView):
    model = Attachment
    template_name = 'mainapp/attachment_list.html'
    context_object_name = 'attachment_list'

class AttachmentDetailView(DetailView):
    model = Attachment
    template_name = 'mainapp/attachment_detail.html'
    context_object_name = 'attachment'

class AttachmentCreateView(CreateView):
    model = Attachment
    fields = ['file', 'message']

    template_name = 'mainapp/attachment_form.html'
    success_url = reverse_lazy('attachment_list')

class AttachmentUpdateView(UpdateView):
    model = Attachment
    fields = ['file', 'message']

    template_name = 'mainapp/attachment_form.html'
    success_url = reverse_lazy('attachment_list')

class AttachmentDeleteView(DeleteView):
    model = Attachment
    template_name = 'mainapp/attachment_confirm_delete.html'
    success_url = reverse_lazy('attachment_list')

class LabelListView(ListView):
    model = Label
    template_name = 'mainapp/label_list.html'
    context_object_name = 'label_list'

class LabelDetailView(DetailView):
    model = Label
    template_name = 'mainapp/label_detail.html'
    context_object_name = 'label'

class LabelCreateView(CreateView):
    model = Label
    fields = ['name', 'user']

    template_name = 'mainapp/label_form.html'
    success_url = reverse_lazy('label_list')

class LabelUpdateView(UpdateView):
    model = Label
    fields = ['name', 'user']

    template_name = 'mainapp/label_form.html'
    success_url = reverse_lazy('label_list')

class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'mainapp/label_confirm_delete.html'
    success_url = reverse_lazy('label_list')

class NoteLabelListView(ListView):
    model = NoteLabel
    template_name = 'mainapp/notelabel_list.html'
    context_object_name = 'notelabel_list'

class NoteLabelDetailView(DetailView):
    model = NoteLabel
    template_name = 'mainapp/notelabel_detail.html'
    context_object_name = 'notelabel'

class NoteLabelCreateView(CreateView):
    model = NoteLabel
    fields = ['note', 'label']

    template_name = 'mainapp/notelabel_form.html'
    success_url = reverse_lazy('notelabel_list')

class NoteLabelUpdateView(UpdateView):
    model = NoteLabel
    fields = ['note', 'label']

    template_name = 'mainapp/notelabel_form.html'
    success_url = reverse_lazy('notelabel_list')

class NoteLabelDeleteView(DeleteView):
    model = NoteLabel
    template_name = 'mainapp/notelabel_confirm_delete.html'
    success_url = reverse_lazy('notelabel_list')
