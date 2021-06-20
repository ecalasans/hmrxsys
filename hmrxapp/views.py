from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, '../hmrxapp/static/login.html')

@csrf_exempt
def sysLogin(request):
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        # Autentica usuário com as informações passadas
        user = authenticate(request, username=request.POST['usuario'],
                            password=request.POST['senha'])
        print(request.POST['usuario'])
        # Se o usuário existir realiza o login
        if user is not None:
            login(request, user)
            print(request.user.id)
            return JsonResponse(
                {'resposta': 'logado',
                 'usuario': request.user.first_name}, safe=False)
        else:
            return HttpResponse({'resposta': 'nao_logado'}, safe=False)
