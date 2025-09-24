from django.http import HttpResponse, JsonResponse
from django.views import View

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
