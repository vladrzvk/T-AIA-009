from rest_framework import serializers
from .models import Genre, Book, Ville, Gare, Voyage, Train

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = "__all__"
  

class VilleSerializer(serializers.ModelSerializer):
    ville_nom = serializers.CharField(source='ville.nom', read_only=True)
    class Meta:
        model = Ville
        fields = '__all__'
        
    def create(self, validated_data):
        # La création d'une nouvelle gare nécessite également de créer la ville si elle n'existe pas
        ville_data = validated_data.pop('ville', None)
        if ville_data:
            ville, created = Ville.objects.get_or_create(nom=ville_data['nom'])
            validated_data['ville'] = ville

        return Gare.objects.create(**validated_data)
        
class GareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gare
        fields = '__all__'
        
class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'
        
class VoyageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyage
        fields = '__all__'