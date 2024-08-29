from django.urls import reverse
from django.utils import timezone
from django.db import models
import uuid
# Create your models here.


class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField() 
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key


class PermitDocCategory(models.Model):
    """DocumentCategory"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        #verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Citizenship(models.Model):
    """Citizenship"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        #verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name

class AcademicSession(models.Model):
    """Academic Session"""

    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    """Academic Term"""

    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Subject"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class DocumentType(models.Model):
    """DocumentType"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class DirecaoAlocacao(models.Model):
    ESTADO_OBJECTO = [("activo", "Activo"), ("eliminado", "Eliminado")]
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    estado_objecto  = models.CharField(
        max_length=200, choices=ESTADO_OBJECTO, default="activo", verbose_name="estado objecto"
    )


    nome = models.CharField(max_length=200)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
    



class Categoria(models.Model):
    ESTADO_OBJECTO = [("activo", "Activo"), ("eliminado", "Eliminado")]
    TIPO_CATEGORIA = [("nova", "Nova"), ("antiga", "Antiga")]
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)


    nome = models.CharField(max_length=200)

    estado_objecto  = models.CharField(
        max_length=200, choices=ESTADO_OBJECTO, default="activo", verbose_name="estado objecto"
    )
    tipo  = models.CharField(
        max_length=200, choices=TIPO_CATEGORIA, default="antiga", verbose_name="Categoria Laboral"
    )

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome  
    

class FuncaoChefia(models.Model):
    ESTADO_OBJECTO = [("activo", "Activo"), ("eliminado", "Eliminado")]
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)


    nome = models.CharField(max_length=200)
    
    estado_objecto  = models.CharField(
        max_length=200, choices=ESTADO_OBJECTO, default="activo", verbose_name="estado objecto"
    )

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
    

class Departamento(models.Model):
    ESTADO_OBJECTO = [("activo", "Activo"), ("eliminado", "Eliminado")]
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    


    nome = models.CharField(max_length=200, unique=True)
    

    estado_objecto  = models.CharField(
        max_length=200, choices=ESTADO_OBJECTO, default="activo", verbose_name="estado objecto"
    )

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
    





class CategoriaNova(models.Model):
    ESTADO_OBJECTO = [("activo", "Activo"), ("eliminado", "Eliminado")]
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    


    nome = models.CharField(max_length=200, unique=True)
    

    estado_objecto  = models.CharField(
        max_length=200, choices=ESTADO_OBJECTO, default="activo", verbose_name="estado objecto"
    )

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


