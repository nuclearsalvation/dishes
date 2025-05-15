from django import forms
from .models import Note, MasterNote, NoteImage

class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = 'name', 'description', 'body', 'links'
    
    name = forms.CharField(max_length=30)
    description = forms.CharField()
    body = forms.CharField()
    links = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=Note.objects.all(),
    )

class NoteSearchForm(forms.Form):
    tag = forms.CharField()

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = 'name', 'description', 'body', 'links', 'images'
    
    name = forms.CharField(max_length=30)
    description = forms.CharField()
    body = forms.CharField()
    links = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=Note.objects.all(),
    )
    images = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=NoteImage.objects.all(),
    )

class TestFormForm(forms.Form):
    tag = forms.DecimalField()

class MasterNoteCreateForm(forms.ModelForm):
    class Meta():
        model = MasterNote
        fields = 'name', 'description', 'links'
    
    name = forms.CharField(max_length=30)
    description = forms.CharField()
    
    links = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset=Note.objects.all(),
    )