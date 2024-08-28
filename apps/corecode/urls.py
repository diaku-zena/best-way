from django.urls import path

from .views import (
    ClassCreateView,
    ClassDeleteView,
    ClassListView,
    ClassUpdateView,
    CurrentSessionAndTermView,
    IndexView,
    SessionCreateView,
    SessionDeleteView,
    SessionListView,
    SessionUpdateView,
    SiteConfigView,
    SubjectCreateView,
    SubjectDeleteView,
    SubjectListView,
    SubjectUpdateView,
    TermCreateView,
    TermDeleteView,
    TermListView,
    TermUpdateView,
    PermitDocCategoryCreateView,
    PermitDocCategoryDeleteView,
    PermitDocCategoryListView,
    PermitDocCategoryUpdateView,
    CitizenshipCreateView,
    CitizenshipDeleteView,
    CitizenshipListView,
    CitizenshipUpdateView,
    DocumentTypeCreateView,
    DocumentTypeDeleteView,
    DocumentTypeListView,
    DocumentTypeUpdateView,

    FuncaoChefiaListView,
    CategoriaListView,
    DepartamentoListView,
    categoria_list_ajax,
    categoria_nova_list_ajax,
    funcao_chefia_detail,
    funcao_chefia_edit,
    funcao_chefia_list,
    categoria_detail,
    categoria_edit,
    categoria_list,
    categoria_nova_detail,
    categoria_nova_edit,
    categoria_nova_list,
    departamento_detail,
    departamento_edit,
    departamento_list,
    edit_success,
    departamento_add,
    funcao_chefia_add,
    categoria_add,
    categoria_nova_add,
    editFuncaoChefia,
    editCategoria,
    editCategoriaNova,
    editDepartamento,
    index,
    upload_excel_categoria,
    upload_excel_categoria_nova,
    upload_excel_departamento,
    upload_excel_funcao_chefia,
    upload_excel_direcao,
    deleteFuncaoChefia,
    funcao_chefia_delete,
    deleteCategoria,
    categoria_delete,
    deleteCategoriaNova,
   categoria_nova_delete,
    deleteDepartamento,
    departamento_delete,
    direccao_list,
    direccao_add,
    direccao_edit,
    direccao_detail,
    direccao_delete,
    logout_view,
    editDireccao,
    deleteDireccao,
    create_user,
    
    
)



urlpatterns = [
    
    
    path("funcao-chefia-antiga/list/", funcao_chefia_list, name="funcao-chefia-list"),
    path("funcao-chefia-antiga/edit/<uuid:id>", funcao_chefia_edit, name="funcao-chefia-edit"),
    path("funcao-chefia-antiga/detail/<uuid:id>", funcao_chefia_detail, name="funcao-chefia-detail"),
    path("funcao-chefia-antiga-delete/<uuid:id>",funcao_chefia_delete, name="funcao-chefia-delete"),
    path("funcao-chefia-antiga/create/", funcao_chefia_add, name="funcao-chefia-create"),
    path("funcao-chefia-antiga-update/", editFuncaoChefia, name="funcao-chefia-update"),
    path("delete/funcao-chefia", deleteFuncaoChefia, name="funcao-chefia-delete"),

    path("categoria/list/categoria-list-ajax/<int:page>", categoria_list_ajax, name="categoria-list-ajax"),
    path("categoria-list-ajax/<int:page>", categoria_list_ajax, name="categoria-list-ajax"),
    path("categoria-laboral-antiga/list/", categoria_list, name="categoria-list"),
    path("categoria-laboral-antiga/edit/<uuid:id>", categoria_edit, name="categoria-edit"),
    path("categoria-laboral-antiga/detail/<uuid:id>", categoria_detail, name="categoria-detail"),
    path("categoria-laboral-antiga-delete/<uuid:id>",categoria_delete, name="categoria-delete"),
    path("categoria-laboral-antiga/create/", categoria_add, name="categoria-create"),
    path("categoria-laboral-antiga-update/", editCategoria, name="categoria-update"),
    path("delete-categoria/", deleteCategoria, name="categoria-delete"),


    path("funcao-chefia-nova/list/categoria-nova-list-ajax/<int:page>", categoria_nova_list_ajax, name="categoria-nova-list-ajax"),
    path("categoria-nova-list-ajax/<int:page>", categoria_nova_list_ajax, name="categoria-nova-list-ajax"),
    path("funcao-chefia-nova/list/", categoria_nova_list, name="categoria-nova-list"),
    path("funcao-chefia-nova/edit/<uuid:id>", categoria_nova_edit, name="categoria-nova-edit"),
    path("funcao-chefia-nova/detail/<uuid:id>", categoria_nova_detail, name="categoria-nova-detail"),
    path("funcao-chefia-nova-delete/<uuid:id>",categoria_nova_delete, name="categoria-nova-delete"),
    path("funcao-chefia-nova/create/", categoria_nova_add, name="categoria-nova-create"),
    path("funcao-chefia-nova-update/", editCategoriaNova, name="categoria-nova-update"),
    path("delete-funcao-chefia-nova/", deleteCategoriaNova, name="categoria-nova-delete"),


    #l

    path("departamento/edit/<uuid:id>", departamento_edit, name="departamento-edit"),
    path("departamento/detail/<uuid:id>", departamento_detail, name="departamento-detail"),
    path("departamento-delete/<uuid:id>",departamento_delete, name="departamento-delete"),
    path("departamento/list/", departamento_list, name="departamento-list"),
    
    path("departamento/create/", departamento_add, name="departamento-create"),
    path("update-departamento/", editDepartamento, name="departamento-update"),
    path("delete/", deleteDepartamento, name="departamento-delete"),

    #direcoes 
    path("direccao/list/", direccao_list, name="direccao-list"),
    path("direccao/edit/<uuid:id>", direccao_edit, name="direccao-edit"),
    path("direccao/detail/<uuid:id>", direccao_detail, name="direccao-detail"),
    path("direccao-delete/<uuid:id>",direccao_delete, name="direccao-delete"),
    path("direccao/create/", direccao_add, name="direccao-create"),

    path("direccao/create/", direccao_add, name="direccao-create"),
    path("update-direccao/", editDireccao, name="direccao-update"),
    path("delete-direccao/", deleteDireccao, name="direccao-delete"),


       path("user", create_user, name="create-user"),

    path("", index, name="home"),
    path("site-config", SiteConfigView.as_view(), name="configs"),
    path(
        "current-session/", CurrentSessionAndTermView.as_view(), name="current-session"
    ),
    path("session/list/", SessionListView.as_view(), name="sessions"),
    path("session/create/", SessionCreateView.as_view(), name="session-create"),
    path(
        "session/<int:pk>/update/",
        SessionUpdateView.as_view(),
        name="session-update",
    ),
    path(
        "session/<int:pk>/delete/",
        SessionDeleteView.as_view(),
        name="session-delete",
    ),
    path("term/list/", TermListView.as_view(), name="terms"),
    path("term/create/", TermCreateView.as_view(), name="term-create"),
    path("term/<int:pk>/update/", TermUpdateView.as_view(), name="term-update"),
    path("term/<int:pk>/delete/", TermDeleteView.as_view(), name="term-delete"),

    path("class/list/", ClassListView.as_view(), name="classes"),
    path("class/create/", ClassCreateView.as_view(), name="class-create"),
    path("class/<int:pk>/update/", ClassUpdateView.as_view(), name="class-update"),
    path("class/<int:pk>/delete/", ClassDeleteView.as_view(), name="class-delete"),
    path("subject/list/", SubjectListView.as_view(), name="subjects"),
    path("subject/create/", SubjectCreateView.as_view(), name="subject-create"),
    path(
        "subject/<int:pk>/update/",
        SubjectUpdateView.as_view(),
        name="subject-update",
    ),
    path(
        "subject/<int:pk>/delete/",
        SubjectDeleteView.as_view(),
        name="subject-delete",
    ),
    path("permitdoccategory/list/", PermitDocCategoryListView.as_view(), name="permitdoccategory"),
    path("permitdoccategory/create/", PermitDocCategoryCreateView.as_view(), name="permitdoccategory-create"),
    path("permitdoccategory/<int:pk>/update/", PermitDocCategoryUpdateView.as_view(), name="permitdoccategory-update"),
    path("permitdoccategory/<int:pk>/delete/", PermitDocCategoryDeleteView.as_view(), name="permitdoccategory-delete"),
    path("citizenship/list/", CitizenshipListView.as_view(), name="citizenship"),
    path("citizenship/create/", CitizenshipCreateView.as_view(), name="citizenship-create"),
    path("citizenship/<int:pk>/update/", CitizenshipUpdateView.as_view(), name="citizenship-update"),
    path("citizenship/<int:pk>/delete/", CitizenshipDeleteView.as_view(), name="citizenship-delete"),
    path("doctype/list/", DocumentTypeListView.as_view(), name="doctype"),
    path("doctype/create/", DocumentTypeCreateView.as_view(), name="doctype-create"),
    path("doctype/<int:pk>/update/", DocumentTypeUpdateView.as_view(), name="doctype-update"),
    path("doctype/<int:pk>/delete/", DocumentTypeDeleteView.as_view(), name="doctype-delete"),



    path("edit-success/", edit_success, name="edit-success"),
    path('upload_excel_categoria', upload_excel_categoria, name='upload-excel-categoria'),
    path('upload_excel_categoria_nova', upload_excel_categoria_nova, name='upload-excel-categoria-nova'),
    path('upload_excel_funcao-chefia', upload_excel_funcao_chefia, name='upload-excel-funcao-chefia'),
    path('upload_excel_direcao', upload_excel_direcao, name='upload-excel-direcao'),
    path('upload_excel_departamento', upload_excel_departamento, name='upload-excel-departamento'),


   
   




    path("logout-def/", logout_view, name="logout-def"),
]
