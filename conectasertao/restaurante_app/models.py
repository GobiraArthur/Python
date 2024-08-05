from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Categoria (models.Model):
    nome = models.TextField()
    ordem = models.IntegerField(default=0)
    def __str__ (self):
        return self.nome
    class Meta:
        verbose_name_plural = "Categorias"

class Item (models.Model):
    nome = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    tempo_preparo = models.TextField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagem = models.TextField()
    def __str__ (self):
        return self.nome + " - " + self.categoria.nome
    class Meta:
        verbose_name_plural = "Itens"

class ItemCardapio (models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    cardapio = models.ForeignKey('Cardapio', on_delete=models.CASCADE)
    def __str__ (self):
        return self.item.nome + " - " + self.cardapio.nome
    class Meta:
        verbose_name_plural = "ItemCardapio"

class Cardapio (models.Model):
    nome = models.TextField()
    def __str__ (self):
        return self.nome
    class Meta:
        verbose_name_plural = "Cardapios"
