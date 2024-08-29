from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
import hrm_app.settings as sett
import uuid

from apps.corecode.models import (
    PermitDocCategory,
    Citizenship,
    DirecaoAlocacao,
    Categoria,
    CategoriaNova,
    FuncaoChefia,
)


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Estabelecimento")


class Employee(models.Model):
    STATUS_CHOICES = [
        ("activo", "Activo"),
        ("pre-reformado", "Pré-Reformado"),
        ("licenciado", "Licenciado"),
        ("reformado", "Reformado"),
    ]
    ESTADO = [("activo", "Activo"), ("inactivo", "Inactivo"), ("incluso", "Incluso")]
    ORIGEM = [("primavera", "Primavera"), ("incluso", "Incluso")]

    ESTADO_OBJECTO = [("activo", "Activo"), ("eliminado", "Eliminado")]

    ESTADO_PV = [("pendente", "Pendente"), ("feito", "Feito"), ("faltoso", "Faltoso")]
    ESTADO_CIVIL = [
        ("solteiro", "Solteiro(a)"),
        ("casado", "Casado(a)"),
        ("divorciado", "Divorciado(a)"),
        ("viuvo", "Viúvo(a)"),
    ]
    PROVINCIAS = [
        ("Bengo", "Bengo"),
        ("Benguela", "Benguela"),
        ("Bié", "Bié"),
        ("Cabinda", "Cabinda"),
        ("Cuando Cubango", "Cuando Cubango"),
        ("Cuanza Norte", "Cuanza Norte"),
        ("Cuanza Sul", "Cuanza Sul"),
        ("Cunene", "Cunene"),
        ("Huambo", "Huambo"),
        ("Huíla", "Huíla"),
        ("Luanda", "Luanda"),
        ("Lunda Norte", "Lunda Norte"),
        ("Lunda Sul", "Lunda Sul"),
        ("Malanje", "Malanje"),
        ("Moxico", "Moxico"),
        ("Namibe", "Namibe"),
        ("Uíge", "Uíge"),
        ("Zaire", "Zaire"),
    ]

    GENDER_CHOICES = [("masculino", "Мasculino"), ("femenino", "Femenino")]
    TIPO_REFORMA = [
        ("reformado", "Reformado"),
        ("pré-reforma", "Pré-reforma"),
        ("não reformado", "Não reformado"),
    ]

    current_status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default="activo",
        verbose_name="situacao",
    )
    estado = models.CharField(
        max_length=100, choices=ESTADO, default="activo", verbose_name="estado"
    )
    origem = models.CharField(
        max_length=100, choices=ORIGEM, default="incluso", verbose_name="origem"
    )
    personnel_number = models.CharField(
        max_length=2000, unique=True, verbose_name="Número do BI", null=True
    )
    data_de_emissao = models.DateField(
        blank=True, null=True, verbose_name="Data de Emissão do BI"
    )
    data_de_validade = models.DateField(
        blank=True, null=True, verbose_name="Data de Validade do BI"
    )
    numero_mecanografico = models.CharField(
        max_length=2000, unique=True, verbose_name="Número Mecanográfico", null=True
    )
    firstname = models.CharField(max_length=2000, verbose_name="Primeiro Nome")
    surname = models.CharField(max_length=2000, verbose_name="SobreNome")
    idade = models.CharField(max_length=2000, verbose_name="Idade")
    correio_electronico = models.CharField(
        max_length=2000, verbose_name="Correio Electrónico", null=True
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default="masculino",
        verbose_name="Genero",
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Data de Nascimento"
    )
    provincia_residencia = models.CharField(
        max_length=30,
        choices=PROVINCIAS,
        default="Luanda",
        verbose_name="Província de Residência",
    )
    provincia_nascimento = models.CharField(
        max_length=30,
        choices=PROVINCIAS,
        default="Luanda",
        verbose_name="Província de Nascimento",
    )
    naturalidade = models.CharField(
        max_length=30, verbose_name="Naturalidade", null=True
    )
    estado_civil = models.CharField(
        max_length=20,
        choices=ESTADO_CIVIL,
        default="solteiro",
        verbose_name="Estado Cívil",
    )
    localidade = models.CharField(max_length=2000, verbose_name="Localidade", null=True)
    morada = models.CharField(max_length=2000, verbose_name="Morada", null=True)
    numero_dependentes = models.CharField(
        max_length=2000, verbose_name="Número Dependentes", null=True
    )
    telefone = models.CharField(max_length=9, verbose_name="Telefone", null=True)
    habilitacao = models.CharField(
        max_length=2000, verbose_name="Habilitação", null=True
    )
    area_de_formacao = models.CharField(
        max_length=2000, verbose_name="Área de Formação", null=True
    )
    vencimento_mensal = models.CharField(
        max_length=9, verbose_name="Vencimento", null=True
    )
    # numero_inss = models.CharField(max_length=200, unique=True, verbose_name="Número INSS",null=True)

    reforma = models.CharField(
        max_length=20, choices=TIPO_REFORMA, default="reformado", verbose_name="Reforma"
    )
    tempo_na_empresa = models.CharField(max_length=50, default="NaN")

    data_de_admissao = models.DateField(
        blank=True, null=True, verbose_name="Data de Admissão"
    )

    direccao = models.ForeignKey(
        DirecaoAlocacao,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Direção de Alocação",
    )

    # nacionalidade = models.ForeignKey(
    #     Citizenship,
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    #     verbose_name="Nacionalidade",
    # )
    nacionalidade = models.CharField(max_length=50, default="NaN")

    categoria_laboral = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Categoria",
    )

    categoria_nova = models.ForeignKey(
        CategoriaNova,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Categoria Nova",
    )

    data_de_admissao = models.DateField(verbose_name="Data de Demissão", null=True)

    # numero_telefone = models.CharField(
    #    max_length=9, blank=True, verbose_name="Numero de
    # "
    # )

    vinculo_professor = models.CharField(
        max_length=2000, verbose_name="Vinculo Professor", null=True
    )
    curso_ministrado = models.CharField(
        max_length=2000, verbose_name="Curso Ministrado", null=True
    )
    regime_trabalho = models.CharField(
        max_length=2000, verbose_name="Regime Trabalho", null=True
    )

    vinculo_administrativo = models.CharField(
        max_length=2000, verbose_name="Vinculo Administrativo", null=True
    )
    data_de_admissao_administrativo = models.DateField(
        blank=True, null=True, verbose_name="Data de Admissão Administrativo"
    )

    # direccao_administrativo = models.CharField(
    #     max_length=2000, blank=True, null=True, verbose_name="Direção de Alocação Administrativo"
    # )
    # categoria_laboral_administrativo = models.CharField(
    #     max_length=2000, blank=True, null=True, verbose_name="Categoria"
    # )
    # funcao_chefia_administrativo = models.CharField(
    #     max_length=2000, blank=True, null=True, verbose_name="Função de Chefia Administrativo"
    # )

    categoria_laboral_administrativo = models.CharField(
        max_length=2000, blank=True, null=True
    )
    funcao_chefia_administrativo = models.CharField(
        max_length=2000, blank=True, null=True
    )
    direccao_administrativo = models.CharField(max_length=2000, blank=True, null=True)

    def set_categoria_laboral_administrativo(self, categoria):
        self.categoria_laboral_administrativo = str(categoria.id)

    def set_funcao_chefia_administrativo(self, funcao_chefia):
        self.funcao_chefia_administrativo = str(funcao_chefia.id)

    def set_direccao_administrativo(self, direcao):
        self.direccao_administrativo = str(direcao.id)

    vencimento_mensal_administrativo = models.CharField(
        max_length=9, verbose_name="Vencimento Administrativo", null=True
    )

    habilitacao_administrativo = models.CharField(
        max_length=2000, verbose_name="Habilitação", null=True
    )
    area_de_formacao_administrativo = models.CharField(
        max_length=2000, verbose_name="Área de Formação", null=True
    )
    regime_trabalho_administrativo = models.CharField(
        max_length=2000, verbose_name="Regime Trabalho Administrativo", null=True
    )

    profissao = models.CharField(max_length=2000, verbose_name="Profissão", null=True)
    tipo_contrato = models.CharField(
        max_length=2000, verbose_name="Tipo de Contrato", null=True
    )
    tipo_pessoal = models.CharField(
        max_length=2000, verbose_name="Tipo de Pessoal", null=True
    )
    motivo_admissao = models.CharField(
        max_length=2000, verbose_name="Motivo Admissão", null=True
    )
    data_de_demissao = models.DateField(
        blank=True, null=True, verbose_name="Data de Demissão"
    )
    motivo_demissao = models.CharField(
        max_length=2000, verbose_name="Motivo Demissao", null=True
    )

    data_fim_contrato = models.DateField(
        blank=True, null=True, verbose_name="Data de Fim de Contrato"
    )
    anos_trabalho = models.CharField(
        max_length=2000, verbose_name="Anos de Trabalho", null=True
    )
    cargo = models.CharField(max_length=2000, verbose_name="Cargo / Função", null=True)
    situacao_contrato = models.CharField(
        max_length=2000, verbose_name="Efectivo / Contratado", null=True
    )
    carga_horaria_diurna = models.CharField(
        max_length=2000, verbose_name="Carga Horária Diurna", null=True
    )
    carga_horaria_nocturna = models.CharField(
        max_length=2000, verbose_name="Carga Horária Nocturna", null=True
    )
    valor_aula_diurna = models.CharField(
        max_length=2000, verbose_name="Valor Aula Diurna", null=True
    )
    valor_aula_nocturna = models.CharField(
        max_length=2000, verbose_name="Valor Aula Nocturna", null=True
    )
    aula_diurna = models.CharField(
        max_length=2000, verbose_name="Aula Diurna", null=True
    )
    aula_nocturna = models.CharField(
        max_length=2000, verbose_name="Aula Diurna", null=True
    )
    honorario_total = models.CharField(
        max_length=2000, verbose_name="Honorário Total", null=True
    )

    photo = models.ImageField(
        blank=True, upload_to="employees/photos/", verbose_name="Foto"
    )
    

    estado_objecto = models.CharField(
        max_length=200,
        choices=ESTADO_OBJECTO,
        default="activo",
        verbose_name="estado objecto",
    )

    numero_seguranca_social = models.CharField(
        max_length=200, blank=True, verbose_name="Numero de Segurança Social", null=True
    )

    estado_pv = models.CharField(
        max_length=200,
        choices=ESTADO_PV,
        default="pendente",
        verbose_name="estado prova vida",
    )

    funcao_chefia = models.ForeignKey(
        FuncaoChefia,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="funcao de chefia",
    )

    novo_numero_mecanografico = models.CharField(
        max_length=200, unique=True, verbose_name="Novo Número Mecanográfico", null=True
    )

    estado_origem = models.CharField(
        max_length=200,
        choices=ESTADO_PV,
        default="inclusao",
        verbose_name="estado de origem",
    )

 

    class Meta:
        ordering = ["personnel_number", "firstname", "surname"]

    def __str__(self):

        return "{} {}".format(self.firstname, self.surname)

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})


class EmployeeBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file = models.FileField(upload_to="employees/bulkupload/")
