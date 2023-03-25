#from django.shortcuts import render
from agenda.models import Contato
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name =  'agenda/home.html'


class ContatoCreateView(LoginRequiredMixin, CreateView):
    model = Contato
    fields = '__all__'
    template_name = 'agenda/contato_form.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.usuario = user
        return super(ContatoCreateView, self).form_valid(form)
    success_url = reverse_lazy('agenda:home')


class ContatoListView(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'agenda/contato_list.html'
    context_object_name = 'contato'

    def get_queryset(self):

        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)
    

class NomeListView(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'agenda/nome_list.html'
    context_object_name = 'contato'

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            nome = self.request.GET['nome']
        except:
            nome = ''
        # return queryset.filter(usuario=self.request.user).filter(nome__icontains=name)
        return queryset.filter(usuario=self.request.user).filter(nome__icontains=nome)
    

class LetraListView(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'agenda/letra_list.html'
    context_object_name = 'contato'

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            letra = self.request.GET['letra']
        except:
            letra = ''
        return queryset.filter(usuario=self.request.user).filter(nome__startswith=letra)


class ContatoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contato
    success_url = reverse_lazy('agenda:home')

class ContatoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contato
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('agenda:home')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
