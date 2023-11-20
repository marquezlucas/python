import csv
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Alumno, Curso


def cargar_alumnos(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if csv_file.name.endswith('.csv'):
            try:
                decoded_file = csv_file.read().decode('utf-8')
                csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
                next(csv_data)  # si el csv tiene la primera fila de encabezados de columna la saltea
                
                # Lista para almacenar datos serializados de alumnos
                serialized_alumnos = []


                # itera los datos del csv y crea o actualiza los objetos de Alumno
                for row in csv_data:
                    dni, nombre, apellido, telefono, correo_electronico, curso_id = row
                    
                    alumno_exists = Alumno.objects.filter(dni=dni).exists()

                    if alumno_exists:
                        print(f'Alumno with DNI {dni} already exists. Skipping...')
                    else:
                        # crea o actualiza los objetos de Alumno
                        alumno, created = Alumno.objects.update_or_create(
                            dni=dni,
                            defaults={
                                'nombre': nombre,
                                'apellido': apellido,
                                'telefono': telefono,
                                'correo_electronico': correo_electronico,
                                'curso_id': curso_id,
                            }
                        )
                        # Serializar el alumno y agregarlo a la lista
                        serialized_alumno = serialize('json', [alumno], fields=('dni', 'nombre', 'apellido', 'telefono', 'correo_electronico', 'curso'))
                        serialized_alumnos.append(serialized_alumno)

                return JsonResponse({'alumnos': serialized_alumnos, 'message': 'Alumnos cargados correctamente.'}, status=200)
            except ValueError as ve:
                return JsonResponse({'error': str(ve)}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'El archivo debe ser un archivo CSV válido.'}, status=400)
    else:
        return JsonResponse({'error': 'Debe proporcionar un archivo CSV para cargar.'}, status=400)

def listar_alumnos(request):
    alumnos = Alumno.objects.all()

    # Serializa los datos de los alumnos utilizando la función serialize
    serialized_data = serialize('json', alumnos, fields=('nombre', 'apellido', 'dni', 'telefono', 'correo_electronico', 'curso'))

    # Retorna la respuesta en formato JSON
    return JsonResponse({'alumnos': serialized_data}, safe=False)

def obtener_alumno(request, dni):
    if request.method == 'GET':
        alumno = get_object_or_404(Alumno, dni=dni)

        # Serializar el objeto Alumno a formato JSON
        serialized_alumno = serialize('json', [alumno], fields=('nombre', 'apellido', 'dni', 'telefono', 'correo_electronico', 'curso', 'banda_horaria'))

        # Convertir el JSON serializado en un diccionario para JsonResponse
        data = {'alumno': json.loads(serialized_alumno)[0]['fields']}

        return JsonResponse(data, status=200)
    
def modificar_alumno(request, dni):
    if request.method == 'PUT':     #el método PUT se utiliza para actualizar un recurso existente. 
                                    #si el método no es PUT, se devuelve un error 405 Método no permitido utilizando JsonResponse.
        try:   
            data = json.loads(request.body) #la función utiliza json.loads(request.body) para analizar el cuerpo JSON de la solicitud


            alumno = get_object_or_404(Alumno, dni=dni) #se utiliza "get_object_or_404" para obtener el objeto Alumno con el DNI proporcionado. 
                                                        #si no se encuentra un alumno con ese DNI, se devuelve un error 404 No encontrado.
            for key, value in data.items():
                setattr(alumno, key, value) #se utiliza "setattr" para actualizar dinámicamente los atributos del objeto Alumno con los nuevos valores.
            alumno.save()

            return JsonResponse({'message': 'Alumno modificado exitosamente'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_alumno(request, dni):
    if request.method == 'DELETE':
        try:
            alumno = get_object_or_404(Alumno, dni=dni)
            alumno.delete()
            return JsonResponse({'message': 'Alumno eliminado correctamente.'}, status=204)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Devuelve un código de estado 405 (Method Not Allowed) si se utiliza un método no permitido
        return HttpResponseNotAllowed(['DELETE'])

def asignar_curso(request, dni, id_curso):
    if request.method == 'POST':
        try:
            # Obtiene la instancia del alumno y del curso a partir de los parámetros
            alumno = get_object_or_404(Alumno, dni=dni)
            curso = get_object_or_404(Curso, id=id_curso)
            
            # Asigna el curso al alumno y guarda los cambios en la base de datos
            alumno.curso = curso
            alumno.save()

            return JsonResponse({'message': 'Curso asignado exitosamente'}, status=200)

        except Exception as e:
            # Devuelve un mensaje de error si hay algún problema durante el proceso
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Devuelve un código de estado 405 (Method Not Allowed) si se utiliza un método no permitido
        return HttpResponseNotAllowed(['POST'])

def alumnos_por_curso(request, id_curso):
    if request.method == 'GET':
        try:
            # Obtiene la instancia del curso a partir del parámetro
            curso = get_object_or_404(Curso, id=id_curso)
            
            # Filtra los alumnos que pertenecen al curso
            alumnos = Alumno.objects.filter(curso=curso)
            
            # Crea una lista de diccionarios con la información básica de cada alumno
            data = [{'dni': alumno.dni, 'nombre': alumno.nombre} for alumno in alumnos]
            
            return JsonResponse(data, safe=False, status=200)

        except Exception as e:
            # Devuelve un mensaje de error si hay algún problema durante el proceso
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Devuelve un código de estado 405 (Method Not Allowed) si se utiliza un método no permitido
        return HttpResponseNotAllowed(['GET'])
