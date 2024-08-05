from restaurante_app.models import Categoria, Item, Cardapio, ItemCardapio
from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User 

class LoginForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {'password': PasswordInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Login','class':'col form-control my-2 p-2'})
        self.fields['password'].widget.attrs.update({'placeholder':'Senha','class':'col form-control my-2 p-2'})

class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
        widgets = {'password': PasswordInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'required':'True','placeholder':'Login','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['password'].widget.attrs.update({'required':'True','placeholder':'Senha','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['first_name'].widget.attrs.update({'required':'True','placeholder':'Nome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['last_name'].widget.attrs.update({'required':'True','placeholder':'Sobrenome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['email'].widget.attrs.update({'required':'True','placeholder':'Email','class':'col form-control my-2 p-2','autocomplete':'new-password'})

class CategoriaForm (forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {'nome': TextInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder':'Nome da categoria','class':'form-control'})

class ItemForm (forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome','preco','descricao','tempo_preparo','categoria','imagem']
        widgets = {'nome': TextInput(), 'tempo_preparo': TextInput(), 'imagem': TextInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder':'Nome da categoria','class':'form-control'})
        self.fields['preco'].widget.attrs.update({'placeholder':'Preço','class':'form-control'})
        self.fields['descricao'].widget.attrs.update({'placeholder':'Descrição','class':'form-control'})
        self.fields['tempo_preparo'].widget.attrs.update({'placeholder':'Tempo de Preparo','class':'form-control'})
        self.fields['imagem'].widget.attrs.update({'placeholder':'Nome do Arquivo de Imagem','class':'form-control'})
