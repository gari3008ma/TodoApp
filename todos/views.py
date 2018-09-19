from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from .models import Todo, Domain, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging
from .forms import TodoForm

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def home(request):
    return render(request, 'base.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    current_user = request.user
    if user is not None and current_user is not None:
        login(request, user)
        return redirect('/todos/dashboard')
    else:
        return redirect('/todos/login')

@login_required
def index(request):
    # name = email.split('@')[1]
    # data = approval(name)
        user = UserProfile.objects.get(user=request.user)
        user_list = UserProfile.objects.filter(domain = user.domain)
        logger.info(user_list)
        all_todo = Todo.objects.filter(created_by__in = user_list)
        logger.info(all_todo)

        context = {
            'todos':all_todo
         }
        return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TodoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            created_by = UserProfile.objects.get(user=request.user)
            assigned_to = form.cleaned_data['assigned_to']
            deadline = form.cleaned_data['deadline']
            todo = Todo(title=title, text=text, created_by_id=created_by.id, deadline=deadline)
            todo.save()
            return HttpResponseRedirect('/todos/dashboard/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = TodoForm()

    return render(request, 'add.html', {'form': form})


def signup(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            email = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully')
            Domain.objects.create(name = email.split('@')[1])
            UserProfile.objects.create(user=new_user, domain=email.split('@')[1])
            return HttpResponseRedirect('/todos/login/')
    return render(request, 'accounts/signup.html', {
        'user_form': form
    })


def approval(request):
    name = request.POST['name']
    return Domain.objects.filter(body_text__search=name)

