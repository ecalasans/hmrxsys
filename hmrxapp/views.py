from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Filtragem
import json

# Variáveis globais
sess_user_id = 0

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

        # Se o usuário existir realiza o login
        if user is not None:
            login(request, user)
            resposta = 'logado'
            numero_usuario = request.user.id
            fn_usuario = request.user.first_name
            return JsonResponse(
                {'resposta': resposta,
                 'id_usuario': numero_usuario,
                 'usuario': fn_usuario},
                safe=False)
        else:
            return HttpResponse({'resposta': 'nao_logado'}, safe=False)

@csrf_exempt
def saveFilter(request):
    if request.POST:
        # Separa os ajustes
        ajustes = json.loads(request.POST["ajustes"])

        # Cria o registro
        filtro = Filtragem()

        # Preenche os campos
        filtro.avaliador = request.POST["avaliador"]
        filtro.arquivo = request.POST["arquivo"]
        filtro.histograma = request.POST["histograma"]
        filtro.gamma_l = ajustes["gamma_l"]
        filtro.gamma_h = ajustes["gamma_h"]
        filtro.c = ajustes["c"]
        filtro.d0 = ajustes["D0"]

        filtro.save()

        return JsonResponse({
            'status': 'salvo'
        }, safe=False)