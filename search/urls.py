from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookSearchAPI.as_view()),
    # gare 
    # ville
    # train 
    # voyage
    
    path('ville/', views.VilleListCreateAPIView.as_view(), name='ville-list-create'),
    path('gare/', views.GareListCreateAPIView.as_view(), name='gare-list-create'),
    path('train/', views.TrainListCreateAPIView.as_view(), name='train-list-create'), 
    path('voyage/', views.VoyageListCreateAPIView.as_view(), name='voyage-list-create'),
    path('/voyage/fonction/<str:parametre>/', views.VoyageCustomFunction.as_view(), name='voyage-custom-function'),
    

]
