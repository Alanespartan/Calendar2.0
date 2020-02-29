from django import forms
from .models import Session
from djrichtextfield.widgets import RichTextWidget

class AddSessionForm(forms.Form):
    content = forms.CharField(widget=RichTextWidget())