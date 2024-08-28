from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import hrm_app.settings as sett
from django.contrib.auth.models import User
from apps.employees.models import Employee

from apps.corecode.models import Categoria, CategoriaNova,DirecaoAlocacao,FuncaoChefia
#from apps.abertura_prova_vida.models import Abertura_Prova_Vida




class ProvaVida(models.Model):
    ESTADO = [("concluida", "Concluida"), ("anulada", "Anulado")]
    

    estado = models.CharField(
        max_length=10, choices=ESTADO, default="concluida", verbose_name="estado"
    )
 
    
    funcionario = models.ForeignKey(
        Employee, on_delete=models.CASCADE, verbose_name="funcionário"
    )

    abertura_prova_vida = models.ForeignKey(
        'Abertura_Prova_Vida', on_delete=models.CASCADE, verbose_name="Abertura Prova de Vida"
    )
    data_prova_vida = models.DateTimeField(default=timezone.now, verbose_name="Data de prova de vida")

    categoria_nova = models.ForeignKey(
        CategoriaNova, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Categoria Nova"
    )

    novo_numero_mecanografico = models.CharField(max_length=200, verbose_name="Novo Número Mecanográfico",null=True)

    novo_vencimento = models.CharField(max_length=200,  verbose_name="Novo Vencimento",null=True)

    local_prova = models.CharField(max_length=200, verbose_name="Local",null=True)
    observacao = models.CharField(max_length=1000, verbose_name="observacao",null=True)

    


    user= models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name="utilizador"
    )

  
    class Meta:
        ordering = ["estado", "funcionario", "abertura_prova_vida", "data_prova_vida"]

    def __str__(self):
        #return f"{self.surname} {self.firstname} {self.other_name} ({self.registration_number})"
        return "{} {} {}".format(self.funcionario, self.abertura_prova_vida, self.data_prova_vida)

    def get_absolute_url(self):
        return reverse("prova-vida-detail", kwargs={"pk": self.pk})



class Abertura_Prova_Vida(models.Model):
    ESTADOS = [("aberta", "Aberta"), ("fechada", "Fechada")]

    referencia= models.TextField(max_length=400,verbose_name="Referência",unique=True,null=True)



    estado_actual = models.CharField(
        max_length=20, choices=ESTADOS, default="aberta", verbose_name="estado"
    )

 
    data_de_abertura = models.DateField(default=timezone.now, verbose_name="Data de Abertura")
    data_de_fim = models.DateField(default=timezone.now, verbose_name="Data de Fim")
    data_de_fecho= models.DateField(default=timezone.now, verbose_name="Data de Fecho",null=True,blank=True)
    descricao= models.TextField(max_length=400,verbose_name="Descrição",null=True,blank=True)
    provasVida = models.ManyToManyField(ProvaVida, related_name='abertura_prova_vidas')





    def __str__(self):
       
        return "{}".format(self.id)

    def get_absolute_url(self):
        return reverse("abertura-prova-vida-detail", kwargs={"pk": self.pk})



