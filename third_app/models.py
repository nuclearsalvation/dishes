from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=30)
    time = models.DateTimeField()
    description = models.TextField()
    body = models.TextField()
    author = models.CharField(max_length=20)
    links = models.ManyToManyField('self', through='SymmetricalNotes', symmetrical=True)
    images = models.ManyToManyField(to='NoteImage',through='NotesToImage', symmetrical=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('thirdapp:note_one',kwargs={'pk':self.pk})

class SymmetricalNotes(models.Model):
    first = models.ForeignKey(Note, models.CASCADE)
    second = models.ForeignKey(Note, models.CASCADE, related_name='notes')

class MasterNote(models.Model):
    name = models.CharField(max_length=30)
    time = models.DateTimeField()
    description = models.TextField()
    author = models.CharField(max_length=20)
    links = models.ManyToManyField(to='Note',through='NotesToMasterNote', symmetrical=False)

class NotesToMasterNote(models.Model):
    first = models.ForeignKey(MasterNote, models.CASCADE)
    second = models.ForeignKey(Note, models.CASCADE, related_name='notes_to_masternote')



class NoteImage(models.Model):
    img = models.ImageField()

class NotesToImage(models.Model):
    first = models.ForeignKey(Note, models.CASCADE)
    second = models.ForeignKey(NoteImage, models.CASCADE, related_name='images_to_note')