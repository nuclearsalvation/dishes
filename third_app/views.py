from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, View
from .models import Note, SymmetricalNotes, MasterNote, NoteImage
from .forms import NoteCreateForm, NoteSearchForm, NoteUpdateForm, TestFormForm, MasterNoteCreateForm
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
# Create your views here.

class NoteListView(TemplateView):
    template_name = 'third_app/notes_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        return context
    
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.time = datetime.now()
        return super().form_valid(form)
    success_url = reverse_lazy('thirdapp:notes_list')
    
class NoteSearchView(TemplateView):
    form_class = NoteSearchForm
    template_name = 'third_app/search_form'

class NoteListViewSearch(TemplateView):
    model = Note
    template_name = 'third_app/notes_list.html'
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(name__icontains=query) | Note.objects.filter(author__icontains=query)
        return context
    #def get_queryset(self):
    #    query = self.request.GET.get('q')
    #    object_list = Note.objects.filter(name__icontains=query)
    #    return object_list
    
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('thirdapp:notes_list')

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteUpdateForm
    def form_valid(self, form):
        form.instance.author = str(self.request.user)
        form.instance.time = datetime.now()
        return super().form_valid(form)
    success_url = reverse_lazy('thirdapp:notes_list')

class NoteSearchViewAuthor(TemplateView):
    form_class = NoteSearchForm
    template_name = 'third_app/search_by_author.html'

class NoteListViewSearchAuthor(TemplateView):
    model = Note
    template_name = 'third_app/notes_list.html'
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(author__icontains=query)
        return context
    
class NoteListMy(TemplateView):
    model = Note
    template_name = 'third_app/notes_list.html'
    def get_context_data(self, **kwargs):
        query = self.request.user.username
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(author__exact=query)
        return context
    
class NoteLinkedView(View):
    def get(self, request: HttpRequest, pk: int):
        note = get_object_or_404(Note, pk=pk)
        context = {
            'note_req': note
        }
        return render(request, template_name='third_app/notes_linked.html', context=context)
    
class NoteTestView(TemplateView):
    form_class = TestFormForm
    template_name = 'third_app/test_form.html'

class NoteTestResolveView(TemplateView):
    template_name = 'third_app/test_form_resolve.html'
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['test'] = int(query)*10000
        return context

class MasterNoteCreateView(CreateView):
    model = MasterNote
    form_class = MasterNoteCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.time = datetime.now()
        return super().form_valid(form)
    success_url = reverse_lazy('thirdapp:notes_list')

class MasterNoteLinkedView(View):
    def get(self, request: HttpRequest, pk: int):
        masternote = get_object_or_404(MasterNote, pk=pk)
        context = {
            'note_req': masternote
        }
        return render(request, template_name='third_app/masternote_notes_list.html', context=context)
    
class NoteImageCreate(CreateView):
    model = NoteImage
    fields = 'img',

class NoteOneView(TemplateView):
    def get(self, request:HttpRequest, pk:int):
        note = get_object_or_404(Note, pk=pk)
        context = {
            'note': note
        }
        return render(request, template_name='third_app/note_one.html', context=context)
