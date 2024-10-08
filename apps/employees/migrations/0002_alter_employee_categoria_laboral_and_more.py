# Generated by Django 5.0.3 on 2024-07-29 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='categoria_laboral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees_categoria_laboral', to='corecode.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='categoria_laboral_administrativo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adm_categoria_laboral', to='corecode.categoria', verbose_name='Categoria Administrativo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='direccao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees_direccao', to='corecode.direcaoalocacao', verbose_name='Direção de Alocação'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='direccao_administrativo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adm_direcao', to='corecode.direcaoalocacao', verbose_name='Direção de Alocação Administrativo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='funcao_chefia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees_funcao_chefia', to='corecode.funcaochefia', verbose_name='funcao de chefia'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='funcao_chefia_administrativo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adm_funcao_chefia', to='corecode.funcaochefia', verbose_name='Função de Chefia Administrativo'),
        ),
    ]
