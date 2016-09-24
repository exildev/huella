from __future__ import unicode_literals
from django.db import models


class Contratista(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class Contrato(models.Model):
	fecha_inicio = models.DateField(input_formats=['%m/%d/%Y'], )
	fecha_final  = models.DateField(input_formats=['%m/%d/%Y'], )
	contratista = models.ForeignKey(Contratista)
# end class

class Material(models.Model):
	nombre = models.CharField(max_length=100)
	uso_unico = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class TipoAdquisiscion(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class AdquisiscionMaterial(models.Model):
	material = models.ForeignKey(Material)
	orden = models.ForeignKey('OrdenTrabajo')
	tipo = models.ForeignKey(TipoAdquisiscion)
	precio = models.DecimalField(max_digits=15, decimal_places=2)
# end class

class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class OrdenTrabajo(models.Model):
	nombre_corto = models.CharField(max_length=45)
	proyecto = models.ForeignKey(Proyecto)
	contratista = models.ForeignKey(Contrato)
	materiales = models.ManyToManyField(Material, through=AdquisiscionMaterial)
	fecha = models.DateField(input_formats=['%m/%d/%Y'], )
	fecha_creacion = models.DateField(input_formats=['%m/%d/%Y'], auto_now_add=True)
	dependencias = models.ManyToManyField('OrdenTrabajo', blank=True)

	def fecha_final_estimada(self):
		act = Actividad.objects.filter(orden = self).order_by('fecha_estimada').last()
		return act.fecha_estimada
	# e nd def

	def fecha_final_real(self):
		act = Actividad.objects.filter(orden = self).order_by('fecha_completado').last()
		return act.fecha_completado
	# e nd def

	def completado(self):
		acts = Actividad.objects.filter(orden = self)
		if acts.filter(completado=True).count():
			print acts.count(), acts.filter(completado=True).count()
			return 100*acts.filter(completado=True).count()/acts.count()
		# end if
		return 0
	# end def
	def __unicode__(self):
		return "%s" % (self.nombre_corto, )
	# end def
# end class

class Actividad(models.Model):
	nombre = models.CharField(max_length=100)
	orden = models.ForeignKey(OrdenTrabajo)
	completado = models.BooleanField()
	fecha_estimada = models.DateField(input_formats=['%m/%d/%Y'], )
	fecha_completado = models.DateField(input_formats=['%m/%d/%Y'], null=True, blank=True)

	def desface(self):
		if self.fecha_completado and self.fecha_estimada:
			return self.fecha_completado - self.fecha_estimada
		# end def
	# end def
	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class ProgresoGrafico(models.Model):
	orden = models.OneToOneField(OrdenTrabajo)
# end class

class Gantt(models.Model):
	proyecto = models.OneToOneField(Proyecto)
# end class


