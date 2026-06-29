from django.db import models



class Mensagem(models.Model):
    titulo: models.Field = models.CharField(max_length=120)
    conteudo: models.Field = models.TextField()
    criada_em: models.Field = models.DateTimeField(auto_now_add=True)

    # NOVO CAMPO
    autor: models.Field = models.CharField(max_length=80, default="Anônimo")

    class Meta:
        ordering = ['-criada_em',]

    def __str__(self) -> str:
        return self.titulo


