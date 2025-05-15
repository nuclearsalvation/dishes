from django.urls import path
from .views import *

app_name = 'thirdapp'

urlpatterns = [
    path('notes', NoteListView.as_view(template_name='third_app/notes_list.html'), name='notes_list'),
    path('create', NoteCreateView.as_view(template_name='third_app/create_form.html'), name='create_note'),
    path('search', NoteSearchView.as_view(template_name='third_app/search_form.html'), name= 'search_form'),
    path('search_results', NoteListViewSearch.as_view(template_name='third_app/notes_list.html'), name= 'search_results'),
    path('delete/<pk>', NoteDeleteView.as_view(template_name='third_app/delete_confirm.html'), name='delete'),
    path('update/<pk>', NoteUpdateView.as_view(template_name='third_app/update_form.html'), name='update'),
    path('search_by_author_results', NoteListViewSearchAuthor.as_view(template_name='third_app/notes_list.html'), name= 'search_form_author_results'),
    path('search_by_author', NoteSearchViewAuthor.as_view(template_name='third_app/search_by_author.html'), name= 'search_form_author'),
    path('my', NoteListMy.as_view(template_name='third_app/notes_list.html'), name='my_notes'),
    path('linked/<pk>', NoteLinkedView.as_view(), name='linked'),
    path('form_zero', NoteTestView.as_view(template_name='third_app/test_form.html'), name='form_zero'),
    path('form_zero_resolve', NoteTestResolveView.as_view(template_name='third_app/test_form_resolve.html'), name='form_zero_resolve'),
    path('create_masternote', MasterNoteCreateView.as_view(template_name='third_app/create_masternote.html'), name='masternote_create'),
    path('masternote_linked/<pk>', MasterNoteLinkedView.as_view(), name='masternote_linked'),
    path('upload_image', NoteImageCreate.as_view(template_name='third_app/upload_image.html'), name='image_upload'),
    path('note/<pk>', NoteOneView.as_view(template_name='third_app/note_one.html'), name='note_one')

]