from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context, loader



def saludar(request):
    return HttpResponse("Mi primer mensaje desde Django")

def edad(request, edad):

    if edad >= 18:
        return HttpResponse("<h1 style='color:red'>Ud es mayor</h1>")
    else:
        return HttpResponse("<h1 style='color:red'>Ud es menor</h1>")


def probando_template(request):

    datos = {
        'nombre':'pepe',
        'notas':[10,3,4,5,6,3,2,4,7]
    }

    plantilla = loader.get_template("template.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)


    """
    mi_html = open("C:/Users/etiri/Documents/Python/Curso CoderHouse/Clase 17 - 12-05-22/proyecto_uno/proyecto_uno/plantillas/template.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({'nombre': 'Esteban', 'notas':[1,2,3,10,9,3,8,6,7,3,1,0]})
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
    """
