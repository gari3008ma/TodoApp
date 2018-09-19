from django import forms
from bootstrap_datepicker.widgets import DatePicker


class TodoForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    assigned_to = forms.EmailField()
    status = forms.BooleanField()
    deadline = forms.DateField(widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        ))
