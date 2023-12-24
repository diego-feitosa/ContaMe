from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def login(request):
    return HttpResponse("Ola, aqui sera a tela de Login")

def logout(request):
    return HttpResponse("Ola, aqui sera a tela de Logout")

def accounts(request):
    users = User.objects.all()
    return HttpResponse(f"Olá, aqui sera a tela de Visualizar Usuário")

def account(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse(f"Usuário não encontrado")
    return HttpResponse(f"Visualizar os dados de {user.first_name} {user.last_name}")

def create(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST["username"]
        user.password = request.POST["password"]
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.is_staff = request.POST["staff"]
        user.is_active = True
        user.is_superuser = request.POST["admin"]
        return HttpResponse(f"Cadastrando novo usuário {user.first_name} {user.last_name}")
    return HttpResponse(f"Cadastrar novo usuário")

def update(request, id):
    user = User.objects.get(id=id)
    return HttpResponse(f"Atualizar os dados de {user.first_name} {user.last_name}")

def delete(request, id):
    user = User.objects.get(id=id)
    return HttpResponse(f"Olá {user.first_name} {user.last_name}, aqui sera a tela de Apagar Usuário")
