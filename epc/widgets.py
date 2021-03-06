from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from sorl.thumbnail import get_thumbnail
from django.template.loader import render_to_string
from norma.formulario.models import Registro
import models


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            t = get_thumbnail(value, '120x120')
            output.append('<img class="form-cicle" src="{}">'.format(t.url))
            output.append(
                super(AdminFileWidget, self).render(name, value, attrs))
            return mark_safe(u''.join(output))
        # end if
        return super(AdminFileWidget, self).render(name, value, attrs)
    # end def
# end class


class LinearWidget(forms.Widget):

    def __init__(self, orden):
        super(LinearWidget, self).__init__()
        self.orden = orden
    # end def

    def render(self, name, value, attrs=None):
        actividades = models.Actividad.objects.filter(orden = self.orden).order_by('poscicion')
        reals = []
        ests = []
        old_real = 0
        old_est = 0
        for act in actividades:
            if act.completado and act.fecha_completado:
                real = (act.fecha_completado - act.orden.fecha).days# - old_real
                reals.append(real)
                old_real = real
            else:
                reals.append(0)
            # end if
            est = (act.fecha_estimada() - act.orden.fecha).days# - old_est
            ests.append(est)
            old_est = est
        # end for
        return render_to_string("epc/linear.html", {'name': name, 'value': value, 'actividades': actividades, 'reals': reals, 'ests': ests})
    # end def

    class Media:
        js = ('epc/js/chart.js','epc/js/noframework.waypoints.min.js', 'https://cdn.rawgit.com/meetselva/attrchange/master/js/attrchange.js')
    # end class

# end class


class GanttWidget(forms.Widget):

    def __init__(self, proyecto):
        super(GanttWidget, self).__init__()
        self.proyecto = proyecto
    # end def

    def render(self, name, value, attrs=None):
        ordenes = models.OrdenTrabajo.objects.filter(proyecto = self.proyecto)
        return render_to_string("epc/gantt.html", {'name': name, 'value': value, 'ordenes': ordenes})
    # end def


# end class

class DependenceWidget(forms.Widget):

    def __init__(self):
        super(DependenceWidget, self).__init__()
    # end def

    def render(self, name, value, attrs=None):
        return render_to_string("epc/dependence.html", {'name': name, 'value': value, 'choices': self.choices.queryset})
    # end def

    class Media:
        js = (
            'epc/js/selectize.min.js',
            'epc/js/jqueryui.js',
        )
        css = {
            'all': ('epc/css/selectize.default.css', )
        }
    # end class

# end class

class OrdenableWidget(forms.Widget):

    def __init__(self):
        super(OrdenableWidget, self).__init__()
    # end def

    def render(self, name, value, attrs=None):
        return render_to_string("epc/ordenable.html", {'name': name, 'value': value})
    # end def

    class Media:
        js = (
            'epc/js/jqueryui.js',
            'epc/js/sortable.js',
        )
    # end class
# end class


class FillFormatWidget(forms.Widget):

    def __init__(self):
        super(FillFormatWidget, self).__init__()
    # end def

    def render(self, name, value, attrs=None):
        #registro = Registro.objects.filter(pk = value).first()
        return render_to_string("epc/fillformat.html", {'name': name, 'value': value})
    # end def

# end class



