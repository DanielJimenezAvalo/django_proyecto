from decimal import Context
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from matplotlib.style import context
from django.template import loader
from django.shortcuts import render

class Persona():
    def __init__(self,nombre,apellido):
        
        self.nombre=nombre
        
        self.apellido=apellido


def saludo(request): #primera vista
    
    #return HttpResponse('hola alumnos esta es nuestra primera pagina con django')
    p1=Persona('profesor Daniel','jimenez')
    
    #nombre = 'Daniel'
    
    #apellido='Jimenez'
    
    temasDelCurso=['plantillas','modelos','formularios','vistas','despliegue']
    
    ahora=datetime.datetime.now()
       
    #doc_externo=open('/home/daniel/Documents/Curso_pildoras_informaticas/curso_django/ProyectoDjango/Proyecto1/Proyecto1/pantillas/miplantilla.html')

    #plt=Template(doc_externo.read())
    
    #doc_externo.close()
    
   # doc_externo=loader.get_template('miplantilla.html')
    
    #ctx=Context({'nombre_persona':p1.nombre,
    #             'apellido_persona':p1.apellido,
    #             'momento_actual':ahora,
    #             'temas':temasDelCurso})
    
  #  documento=doc_externo.render({'nombre_persona':p1.nombre,
  #                              'apellido_persona':p1.apellido,
  #                              'momento_actual':ahora,
  #                              'temas':temasDelCurso})
    
  #  return HttpResponse(documento)
    return render(request,'miplantilla.html',{'nombre_persona':p1.nombre,
                                            'apellido_persona':p1.apellido,
                                            'momento_actual':ahora,
                                            'temas':temasDelCurso})
def cursoC(request):
    
    fecha_actual=datetime.datetime.now()
    
    return render(request,'cursoC.html',{"dameFecha":fecha_actual})

def cursoCss(request):
    
    fecha_actual=datetime.datetime.now()
    
    return render(request,'cursoCss.html',{"dameFecha":fecha_actual})

def despedida(request):
    
    return HttpResponse('hasta luego alumnos')

def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales  %s
    </h1>
    </body>
    </html>
    """ % fecha_actual
    
    return HttpResponse(documento)
    
def calculaEdad(request,edad,agno):
    
    #edadActual=18
    
    periodo=agno-2022
    
    edadFutura=edad+periodo
    
    documento="<html><body><h2>En el año %s tendras %s años" %(agno,edadFutura)
    
    return HttpResponse(documento)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    