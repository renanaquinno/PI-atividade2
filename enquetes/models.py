from django.db import models

# Create your models here.
class Enquete(models.Model):
        texto = models.CharField(max_length=30) 
        dt_publicacao = models.DateField() 

class Usuario(models.Model):
        email = models.EmailField(max_length=30)
        senha = models.CharField(max_length=255)
        dt_nascimento = models.DateField()

class Perfil(models.Model):
        nome = models.CharField(max_length=20)
        usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Postagem(models.Model):
        texto = models.TextField(max_length=200)
        dt_publicacao = models.DateField() 
        perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='postagens')

class Comentario(models.Model):
        texto = models.TextField(max_length=20)
        dt_publicacao = models.DateField()
        perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='comentarios')
        postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='comentarios')
        respostas = models.ForeignKey('Comentario', on_delete=models.CASCADE)

class Reacao(models.Model):
        REACAO = (
                ("Gostar","gostar"),
                ("Amor","amor"),
                ("Engraçado","engracado"),
                ("Raiva","raiva")
        )
        tipo = models.CharField(choices=REACAO, default=REACAO[0][1], max_length=10)
        data = models.DateField()
        postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='reacoes')
        perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='reacoes')