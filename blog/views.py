from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from datetime import date

from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm

# Create your views here.
class ActivityTwo(View):
    def wellCome(request):
        return HttpResponse("Bem-vindo ao meu blog!")
    
    def eco(request, msg):
        return HttpResponse(f'Você digitou: {msg}')
    
    def api_info(request):
        data =  {
            "disciplina": "RAD",
            "framework": "Django",
            "semestre": "2025.2"
        }
        return JsonResponse(data)
    
class ActivityThree(View):
    def home(request):
        contexto = {
            "usuario" : "Bruno",
            "numb" : 10,
            "now": date.today(),
            "is_logged_in" : True,
            "idade": 17,
            "role" : "admin",
            "produtos" : [
                {
                    "nome" : "feijao",
                    "preco": 10
                },
                {
                    "nome" : "arroz",
                    "preco": 5
                },
                {
                    "nome" : "macarrao",
                    "preco": 15
                },
            ]
        }
        return render(request, "blog/index.html", contexto)
    
    def contato(request, ctt):
        contexto = {
            "contato" : ctt
        }
        return render(request, "blog/contato.html", contexto)
    
    def homeTemplate(request):
        return render(request, "home.html")
    
    def aboutTemplate(request):
        return render(request, "about.html")


# def wellCome(request):
#    return HttpResponse("Bem-vindo ao meu blog!")
    
# def eco(request, msg):
#     return HttpResponse(f'Você digitou: {msg}')
    
# def api_info(request):
#     data =  {
#             "disciplina": "RAD",
#             "framework": "Django",
#             "semestre": "2025.2"
#     }
#     return JsonResponse(data)


# ================== VIEWS CRUD PARA AUTOR ==================
class AutorListView(ListView):
    model = Autor
    template_name = 'blog/autor_list.html'
    context_object_name = 'autores'
    paginate_by = 10

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'blog/autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'blog/autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'blog/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')


# ================== VIEWS CRUD PARA EDITORA ==================
class EditoraListView(ListView):
    model = Editora
    template_name = 'blog/editora_list.html'
    context_object_name = 'editoras'
    paginate_by = 10

class EditoraCreateView(CreateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'blog/editora_form.html'
    success_url = reverse_lazy('editora_list')

class EditoraUpdateView(UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'blog/editora_form.html'
    success_url = reverse_lazy('editora_list')

class EditoraDeleteView(DeleteView):
    model = Editora
    template_name = 'blog/editora_confirm_delete.html'
    success_url = reverse_lazy('editora_list')


# ================== VIEWS CRUD PARA LIVRO ==================
class LivroListView(ListView):
    model = Livro
    template_name = 'blog/livro_list.html'
    context_object_name = 'livros'
    paginate_by = 10

class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'blog/livro_form.html'
    success_url = reverse_lazy('livro_list')

class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'blog/livro_form.html'
    success_url = reverse_lazy('livro_list')

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'blog/livro_confirm_delete.html'
    success_url = reverse_lazy('livro_list')


# ================== VIEWS CRUD PARA PUBLICA ==================
class PublicaListView(ListView):
    model = Publica
    template_name = 'blog/publica_list.html'
    context_object_name = 'publicacoes'
    paginate_by = 10

class PublicaCreateView(CreateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'blog/publica_form.html'
    success_url = reverse_lazy('publica_list')

class PublicaUpdateView(UpdateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'blog/publica_form.html'
    success_url = reverse_lazy('publica_list')

class PublicaDeleteView(DeleteView):
    model = Publica
    template_name = 'blog/publica_confirm_delete.html'
    success_url = reverse_lazy('publica_list')


# ================== DASHBOARD PRINCIPAL ==================
def dashboard(request):
    context = {
        'total_autores': Autor.objects.count(),
        'total_editoras': Editora.objects.count(),
        'total_livros': Livro.objects.count(),
        'total_publicacoes': Publica.objects.count(),
    }
    return render(request, 'blog/dashboard.html', context)

