from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from datetime import date

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
