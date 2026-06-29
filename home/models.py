from django.db import models



class Mensagem(models.Model):
    titulo: models.Field = models.CharField(max_length=120)
    conteudo: models.Field = models.TextField()
    criada_em: models.Field = models.DateTimeField(auto_now_add=True)
    autor: models.Field = models.CharField(max_length=80, default="Anônimo")

    categoria: models.Field = models.ForeignKey(
        "Categoria",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mensagens",
    )

    tags = models.ManyToManyField(
        "Tag",
        blank=True,
        related_name="tags",
    )

    class Meta:
        ordering = ['-criada_em',]

    def __str__(self) -> str:
        return self.titulo


class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["nome", ]

    def __str__(self) -> str:
        return self.nome


class Tag(models.Model):
    nome: models.Field = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ["nome", ]

    def __str__(self) -> str:
        return self.nome



