from django.urls import path
from .views import EstadoCreate, CidadeCreate, EmailSuportCreate, FornecedorCreate, FuncionarioCreate, PrefixoMaquinaCreate, ProdutoCreate
# from .views import NomeCreate
# from .views import NomeUpdate   
# from .views import NomeDelete
# from .views import NomeList
# from .views import IndexView, SobreView, AjudaView, IndexAdmView


urlpatterns = [

    ####################### Adicionar ###################################

    path('cadastrar/estados', EstadoCreate.as_view(), 
        name='cadastrar-estado'),
    path('cadastrar/produto', ProdutoCreate.as_view(), 
        name='cadastrar-produto'),
    path('cadastrar/cidade', CidadeCreate.as_view(),
         name='cadastrar-cidade'),
    path('cadastrar/funcionario', FuncionarioCreate.as_view(),
         name='cadastrar-funcionario'),
    path('cadastrar/fornecedor', FornecedorCreate.as_view(),
         name='cadastrar-fornecedor'),
    path('cadastrar/maquina', PrefixoMaquinaCreate.as_view(),
         name='cadastrar-prefixomaquina'),
    path('cadastrar/EmailSuport', EmailSuportCreate.as_view(),
         name='cadastrar-EmailSuport'),

    

    












]
