from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    assigned_to = forms.EmailField()
    status = forms.BooleanField()
    deadline = forms.DateField()
