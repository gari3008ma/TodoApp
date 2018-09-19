from django import forms


class TodoForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    created_by = forms.EmailField()
    assigned_to = forms.EmailField()
    status = forms.BooleanField()
    deadline = forms.DateTimeField()
