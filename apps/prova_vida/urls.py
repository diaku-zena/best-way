from django.urls import path



from .views import (

    ProvaVidaCreateView,
    ProvaVidaDeleteView,
    ProvaVidaDetailView,
    ProvaVidaListView,
    ProvaVidaUpdateView,
    ProvaGetFuncDetailView,
    getFunc,
    provaGetFuncDetail,
    efectuarProvaVida,
    getProvaVidasFunc,
    getProvaVidasRelatorio,
    prova_vida_func_detail,
    Abertura_Prova_Vida,
  
    Abertura_Prova_VidaCreateView,
    Abertura_Prova_VidaDeleteView,
    Abertura_Prova_VidaDetailView,
    Abertura_Prova_VidaListView,
    Abertura_Prova_VidaUpdateView,
    abrirProvaVida,
    PrivaVidaForm,
    DownloadCSVViewdownloadcsv,
    getProvaVida,
    fecharProvaVida,
    provaVidaForm,
    provaVidaReabrirForm,
    reabrirProvaVida,
    export_to_excel,
    gerarProvaVidaPDF,
    gerarProvaVidaFaltosoPDF,
    export_to_excel_faltoso,
    upload_excel_prova_vida,
    editarProvaVida,
    prova_vida_edit

    # employee_edit, 
    # editFuncionario,


)

urlpatterns = [
    path("list", getProvaVidasFunc, name="prova-vida-list"),
    path("<int:pk>/", ProvaVidaDetailView.as_view(), name="prova-vida-detail"),
    path("create/", ProvaVidaCreateView.as_view(), name="prova-vida-create"),
    path("<int:pk>/update/", ProvaVidaUpdateView.as_view(), name="prova-vida-update"),
    path("<int:pk>/delete/", ProvaVidaDeleteView.as_view(), name="prova-vida-delete"),
    path("<int:pk>/delete/", ProvaVidaDeleteView.as_view(), name="prova-vida-delete"),
    path("getfunc/", getFunc, name="prova-getfunc"),
    path("getfuncetail/", provaGetFuncDetail, name="prova-vida-func"),
    path("saveprovavida/", efectuarProvaVida, name="prova-vida-efectuar"),

    path("relatorio-prova-vida/<int:id>", getProvaVidasRelatorio, name="relatorio-prova-vida"),
    path("prova-vida-func/detail/<int:id>", prova_vida_func_detail, name="prova-vida-func-detail"),

    path("prova-vida-func/edit/<int:id>",prova_vida_edit, name="prova-vida-func-edit"),
    path("update/",editarProvaVida, name="prova-vida-update"),

    #  path("employee-edit/<int:id>",employee_edit, name="employee-edit"),
    #  path("update/",editFuncionario, name="employee-update"),



#for abertura

    path("list", Abertura_Prova_VidaListView.as_view(), name="abertura-prova-vida-list"),
    path("<int:pk>/", Abertura_Prova_VidaDetailView.as_view(), name="abertura-prova-vida-detail"),
    path("create/", Abertura_Prova_VidaCreateView.as_view(), name="abertura-prova-vida-create"),
    path("<int:pk>/update/", Abertura_Prova_VidaUpdateView.as_view(), name="abertura-prova-vida-update"),
    path("<int:pk>/delete/", Abertura_Prova_VidaDeleteView.as_view(), name="abertura-prova-vida-delete"),
    path("upload/", DownloadCSVViewdownloadcsv.as_view(), name="abertura-prova-vida-upload"),
    path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
    path("fechar-prova-vida/", getProvaVida, name="abertura-fecho"),
    path("confirmar-fecho/", fecharProvaVida, name="confirmar-fecho"),
    path("prova-resumo/", abrirProvaVida, name="abertura-prova-vida-resumo"),
    path("prova_vida_form", provaVidaForm, name="abertura-prova-vida-form"),
    path("prova-prorrogar/", abrirProvaVida, name="abertura-prova-vida-prorrogar"),
    path("prova-reabrir-vida-form", provaVidaReabrirForm, name="abertura-prova-vida-reabrir"),
    path("prova-reabrir", reabrirProvaVida, name="prova-vida-reabrir"),
    path("relatorio-prova-vida/", getProvaVidasRelatorio, name="relatorio-prova-vida"),

    path("prova-vida-pdf", gerarProvaVidaPDF, name="prova-vida-pdf"),
    path("prova-vida-f-pdf", gerarProvaVidaFaltosoPDF, name="prova-vida-f-pdf"),
    

    path('export_to_excel_prova_vida', export_to_excel, name='export-excel-prova-vida'),
    path('import_to_excel_prova_vida', upload_excel_prova_vida, name='import-excel-prova-vida'),
  

    

 

]
 