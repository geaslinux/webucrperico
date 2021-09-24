from django.shortcuts import render, HttpResponse 


# Create your views here.


def inicio(Request): 

    return render(Request, "Core/Inicio.html")


def quienessomos(Request): 

    return render(Request, "Core/Quienes Somos.html")

def referentes(Request): 

    return render(Request, "Core/Referentes.html")


def noticias(Request): 

    return render(Request, "Core/Noticias.html")

def proyectos(Request): 

    return render(Request, "Core/Proyectos.html")

def contacto(Request): 

    return render(Request, "Core/Contacto.html")



