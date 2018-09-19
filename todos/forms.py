from django import forms
from django.db import models
from .models import UserProfile, Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['created_by', 'created_at']

    def __init__(self, domain, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.domain = domain
        self.fields['assigned_to'].queryset = UserProfile.objects.filter(domain = domain)




