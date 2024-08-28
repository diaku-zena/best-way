from django.urls import path

from apps.prova_vida.views import export_to_excel_faltoso

from .views import (
    DownloadCSVViewdownloadcsv,
    EmployeeBulkUploadView,
    EmployeeCreateView,
    EmployeeDeleteView,
    EmployeeDetailView,
    EmployeeListView,
    EmployeeUpdateView,
    employee_detail,
    employee_edit,   
    employee_list,
    addFuncionario,
    editFuncionario,
    upload_excel,
    gerarPDF,
    gerarLicenciadosPDF,
    gerarPreReformaPDF,
    deleteFuncionario,
    employee_delete,
    get_employee_report,
    employee_list_type,
    employee_list_pv,
    employee_list_ajax,
    export_to_excel,
    export_to_excel_licenciados,
    export_to_excel_pre_reformados,
    
    
     
)

urlpatterns = [
    path("list", employee_list, name="employee-list"),
    path("employee-list-ajax/<int:page>", employee_list_ajax, name="employee-list-ajax"),

    path("employee-list-type/<str:tipo>", employee_list_type, name="employee-list-type"),
    path("employee-detail/<int:id>", employee_detail, name="employee-detail"),
    path("employee-edit/<int:id>",employee_edit, name="employee-edit"),
    path("employee-delete/<int:id>",employee_delete, name="employee-delete"),
    path("create/", addFuncionario, name="employee-create"),
    path("update/",editFuncionario, name="employee-update"),
    path("delete/", deleteFuncionario, name="employee-delete"),
    #path("upload/", EmployeeBulkUploadView.as_view(), name="employee-upload"),
    path('upload/', upload_excel, name='upload_excel'),
    path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),

    path("funcionario-pdf", gerarPDF, name="funcionario-pdf"),
    path("funcionario-licenciado-pdf", gerarLicenciadosPDF, name="funcionario-licenciado-pdf"),
    path("funcionario-pre-reforma-pdf", gerarPreReformaPDF, name="funcionario-pre-reforma-pdf"),
    path("funcionario-relatorio", get_employee_report, name="funcionario-relatorio"),

    path("employee-list-pv/<str:tipo>", employee_list_pv, name="employee-list-pv"),
 
    path('export_to_excel_funcionarios', export_to_excel, name='export-excel-funcionarios'),
    path('export_to_excel_funcionarios-licenciados', export_to_excel_licenciados, name='export-excel-funcionarios-licenciados'),
    path('export_to_excel_funcionarios-pre-reforma', export_to_excel_pre_reformados, name='export-excel-funcionarios-pre-reforma'),
    path('export_to_excel_funcionarios_faltosos', export_to_excel_faltoso, name='export-excel-funcionarios-faltosos'),
]
