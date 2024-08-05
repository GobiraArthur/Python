from django.shortcuts import render
from restaurante_app.models import Cardapio
from restaurante_app.forms import CategoriaForm, ItemForm, LoginForm,UserForm
from django.http import HttpResponseRedirect, QueryDict
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 

# Create your views here.
def index (request):
    context = {
                "cardapios": Cardapio.objects.all(),
                'loginform' :  LoginForm(),
                'userform' : UserForm(),
            }
    if request.user.is_authenticated:
        context['userform'] = UserForm(instance=User.objects.get(id=request.user.id))
    
    return render(request,'index.html', context)

def login (request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            auth_login(request, user = user)
    return HttpResponseRedirect(reverse('index'))

def logout (request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def newuser (request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            if user.data.get('password') != user.data.get('confirmacao'):
                user.add_error('password','A senha e confirmação devem ser iguais')
            else:
                user = user.save(commit=False)
                user.password = make_password(user.password)
                user.save()
                return HttpResponseRedirect(reverse('index'))
        context = {
                "cardapios": Cardapio.objects.all(),
                'loginform' :  LoginForm(),
                'userform' : user,
        }
        return render(request,'index.html',context)
    return HttpResponseRedirect(reverse('index'))

def deluser (request, id):
    user = User.objects.get(id=id)
    user.delete()
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def editperfil (request):
    if request.method == 'POST':
        usuario = User.objects.get(id=request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario['password'] = usuario.password
        novo_usuario['username'] = usuario.username
        user = UserForm(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
    return HttpResponseRedirect(reverse('index'))