from django.db import models
from django.contrib.auth.models import User


class categorias(models.Model):
	nombre		= models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class noticias(models.Model): 
	titulo		= models.CharField(max_length=100)
	categoria   = models.ForeignKey(categorias)
	fecha       = models.DateField()
	descripcion	= models.TextField(max_length=500)
	imagen 		= models.ImageField(upload_to='noticias')
	autor 		= models.ForeignKey(User)
	estado		= models.BooleanField(default=True)

	def __unicode__(self):
		return self.titulo