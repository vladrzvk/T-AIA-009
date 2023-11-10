from django.db import models

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=60)
	price = models.DecimalField(decimal_places=2, max_digits=4)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Ville(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
    
class Gare(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    

class Train(models.Model):
    depart = models.ForeignKey(Gare, related_name='trains_depart', on_delete=models.CASCADE)
    arrivee = models.ForeignKey(Gare, related_name='trains_arrivee', on_delete=models.CASCADE)
    escales = models.ManyToManyField(Gare)

    def __str__(self):
        return f'Train {self.id}'
    
class Voyage(models.Model):
    depart = models.ForeignKey(Gare, related_name='voyages_depart', on_delete=models.CASCADE)
    arrivee = models.ForeignKey(Gare, related_name='voyages_arrivee', on_delete=models.CASCADE)
    escales = models.ManyToManyField(Gare)

    def __str__(self):
        return f'Voyage {self.id}'