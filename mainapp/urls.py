from django.urls import path
from .views import crud

urlpatterns = [
    # Note URLs
    path('note/', crud.NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', crud.NoteDetailView.as_view(), name='note_detail'),
    path('note/create/', crud.NoteCreateView.as_view(), name='note_create'),
    path('note/<int:pk>/update/', crud.NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', crud.NoteDeleteView.as_view(), name='note_delete'),

    # Conversation URLs
    path('conversation/', crud.ConversationListView.as_view(), name='conversation_list'),
    path('conversation/<int:pk>/', crud.ConversationDetailView.as_view(), name='conversation_detail'),
    path('conversation/create/', crud.ConversationCreateView.as_view(), name='conversation_create'),
    path('conversation/<int:pk>/update/', crud.ConversationUpdateView.as_view(), name='conversation_update'),
    path('conversation/<int:pk>/delete/', crud.ConversationDeleteView.as_view(), name='conversation_delete'),

    # Message URLs
    path('message/', crud.MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', crud.MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', crud.MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', crud.MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', crud.MessageDeleteView.as_view(), name='message_delete'),

    # Attachment URLs
    path('attachment/', crud.AttachmentListView.as_view(), name='attachment_list'),
    path('attachment/<int:pk>/', crud.AttachmentDetailView.as_view(), name='attachment_detail'),
    path('attachment/create/', crud.AttachmentCreateView.as_view(), name='attachment_create'),
    path('attachment/<int:pk>/update/', crud.AttachmentUpdateView.as_view(), name='attachment_update'),
    path('attachment/<int:pk>/delete/', crud.AttachmentDeleteView.as_view(), name='attachment_delete'),

    # Label URLs
    path('label/', crud.LabelListView.as_view(), name='label_list'),
    path('label/<int:pk>/', crud.LabelDetailView.as_view(), name='label_detail'),
    path('label/create/', crud.LabelCreateView.as_view(), name='label_create'),
    path('label/<int:pk>/update/', crud.LabelUpdateView.as_view(), name='label_update'),
    path('label/<int:pk>/delete/', crud.LabelDeleteView.as_view(), name='label_delete'),

    # NoteLabel URLs
    path('notelabel/', crud.NoteLabelListView.as_view(), name='notelabel_list'),
    path('notelabel/<int:pk>/', crud.NoteLabelDetailView.as_view(), name='notelabel_detail'),
    path('notelabel/create/', crud.NoteLabelCreateView.as_view(), name='notelabel_create'),
    path('notelabel/<int:pk>/update/', crud.NoteLabelUpdateView.as_view(), name='notelabel_update'),
    path('notelabel/<int:pk>/delete/', crud.NoteLabelDeleteView.as_view(), name='notelabel_delete'),

]