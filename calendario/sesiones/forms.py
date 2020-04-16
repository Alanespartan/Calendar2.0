from django import forms
from .models import Session
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AddSessionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs=
        {
            'class' : 'form-control',
            'id' : 'session-name',
            'placeholder': 'Introducción a la clase'
        }))
    isClass = forms.BooleanField(required=False)
    content = forms.CharField(widget=CKEditorWidget())
