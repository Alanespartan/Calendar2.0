from django import forms
from .models import Session
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AddSessionForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget())