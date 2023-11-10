from django.shortcuts import render
from .models import Book
from rest_framework import generics, filters, status
from .serializers import BookSerializer
from .models import Ville, Gare, Voyage, Train
from .serializers import VilleSerializer, GareSerializer, TrainSerializer, VoyageSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import ma_fonction 
# Create your views here.

class BookSearchAPI(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['name',]
	queryset = Book.objects.all()
	serializer_class = BookSerializer
 
class BookSearch(generics.ListCreateAPIView):
	filter_backends = (filters.SearchFilter,)
	search_fields = ['id',]
	queryset = Book.objects.all()
	serializer_class = BookSerializer



class VilleListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ['nom','ville',]
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer

# class VilleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ['nom','ville',]
#     queryset = Ville.objects.all()
#     serializer_class = VilleSerializer
    
class GareListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ['nom', 'ville',]
    queryset = Gare.objects.all()
    serializer_class = GareSerializer
    
    def post(self, request, *args, **kwargs):
        noms = request.data.get('nom')
        ville_id = request.data.get('ville')
        print(ville_id)
        ville, created = Ville.objects.get_or_create(nom=ville_id)
        gare = Gare.objects.create(nom=noms, ville=ville)
        serializer = GareSerializer(gare)
        
		# Récupérer les instances de Gare à partir des IDs
		# depart = Gare.objects.get(pk=depart_id)
		# escales = Ville.objects.filter(pk__in=escales_ids)

		# Créer une nouvelle instance de Voyage

		# voyage.escales.set(escales)

		# Serializer pour transformer l'objet Voyage en JSON
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    

		

		


class TrainListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ['depart','arrivee', 'escales',]
    queryset = Ville.objects.all()
    serializer_class = TrainSerializer
    
class VoyageListCreateAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ['depart','arrivee', 'escales',]
    queryset = Ville.objects.all()
    serializer_class = VoyageSerializer
    
    def post(self, request, *args, **kwargs):
        depart_id = request.data.get('depart')
        arrivee_id = request.data.get('arrivee')
        escales_ids = request.data.get('escales', [])

        # Récupérer les instances de Gare à partir des IDs
        depart = Gare.objects.get(pk=depart_id)
        arrivee = Gare.objects.get(pk=arrivee_id)
        escales = Gare.objects.filter(pk__in=escales_ids)

        # Créer une nouvelle instance de Voyage
        voyage = Voyage.objects.create(depart=depart, arrivee=arrivee)
        voyage.escales.set(escales)

        # Serializer pour transformer l'objet Voyage en JSON
        serializer = VoyageSerializer(voyage)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
    
    
class VoyageCustomFunction(APIView):
    def get(self, request, *args, **kwargs):
        parametre = self.kwargs.get('parametre')
        resultat = ma_fonction(parametre)
        return JsonResponse({'resultat': resultat})
    
    