from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,FormView,CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from . import models
from django.urls import reverse_lazy


class CustomLogin(LoginView):
    model=models.Note
    fields='__all__'
    template_name='base/login.html'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('NoteList')
    


def home(request):
    return HttpResponse("hii")

class NoteList(LoginRequiredMixin,ListView):
    model=models.Note
    template_name='base/note_list.html'
    context_object_name='notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)

        return context
    
class NoteCreate(CreateView):
    model=models.Note
    fields=['title', 'description']
    template_name='base/note_create.html'
    redirect_authenticated_user=True
    success_url=reverse_lazy('NoteList')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)

class NoteDetail(LoginRequiredMixin,DetailView):
    model=models.Note
    template_name='base/note_detail.html'
    context_object_name='note'

class NoteEdit(LoginRequiredMixin,UpdateView):
    model=models.Note
    fields='__all__'
    template_name='base/note_edit.html'
    context_object_name='note'

    def get_success_url(self):
        return reverse_lazy('NoteList')
    

class Customregister(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('NoteList')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Customregister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('NoteList')
        return super(Customregister, self).get(*args, **kwargs)
    

    def get_success_url(self):
        return reverse_lazy('NoteList')