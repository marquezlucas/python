import json
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Alumno, Curso
import csv

# Create your views here.
def cargar_alumno(request,dni): #ver de modificar
    alumno = get_object_or_404(Alumno, dni = dni)

def listar_alumno(request, dni):
    alumnos = Alumno.objects.all()

def obtener_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni = dni)

def modificar_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni = dni)

def eliminar_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni = dni)

def asignar_curso(request, dni, id_curso):
    alumno = get_object_or_404(Alumno, dni = dni)

def alumno_por_curso(request, id_curso):
    alumno = get_object_or_404(Alumno)
