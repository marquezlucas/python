import csv
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404 #get_list_or_404
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
                alumnos_data = []


                # itera los datos del csv y crea o actualiza los objetos de Alumno
                for row in csv_data:
                    dni, nombre, apellido, telefono, correo_electronico, curso_id = row
                    
                    alumno_exists = Alumno.objects.filter(dni=dni).exists()

                    # Crea o actualiza los objetos de Alumno
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
                    # Agrega los datos del alumno a la lista
                    alumnos_data.append({
                        'dni': alumno.dni,
                        'nombre': alumno.nombre,
                        'apellido': alumno.apellido,
                        'telefono': alumno.telefono,
                        'correo_electronico': alumno.correo_electronico,
                        'curso': str(alumno.curso),
                    })
                
                return JsonResponse({'alumnos': alumnos_data, 'message': 'Alumnos cargados correctamente.'}, status=200)
            except ValueError as ve:
                logger.error(f'Error al cargar alumnos desde CSV: {ve}')
                return JsonResponse({'error': 'Error en el formato del archivo CSV.'}, status=400)
            except Exception as e:
                logger.error(f'Error al cargar alumnos desde CSV: {e}')
                return JsonResponse({'error': 'Error interno del servidor.'}, status=500)
        else:
            return JsonResponse({'error': 'El archivo debe ser un archivo CSV válido.'}, status=400)
    else:
        return JsonResponse({'error': 'Debe proporcionar un archivo CSV para cargar.'}, status=400)

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    
    # Serializa los datos de los alumnos en una lista de diccionarios
    serialized_alumnos = []
    for alumno in alumnos:
        serialized_alumnos.append({
            'nombre': alumno.nombre,
            'apellido': alumno.apellido,
            'dni': alumno.dni,
            'telefono': alumno.telefono,
            'correo_electronico': alumno.correo_electronico,
            'curso': alumno.curso.nombre if alumno.curso else None,
            'banda_horaria': alumno.curso.banda_horaria.nombre if alumno.curso else None,
        })

def obtener_alumno(request, dni):
    if request.method == 'GET':
        alumno = get_object_or_404(Alumno, dni=dni)

        # Crear una respuesta HTTP con el tipo de contenido CSV
        response = HttpResponse(content_type='text/csv')
        
        # Establecer el encabezado para la descarga del archivo
        response['Content-Disposition'] = 'attachment; filename="alumno.csv"'

        # Crear un objeto escritor CSV
        csv_writer = csv.writer(response)

        # Escribir la fila de encabezado
        csv_writer.writerow(['dni', 'nombre', 'apellido', 'telefono', 'correo_electronico', 'curso', 'banda_horaria'])

        # Escribir los datos del alumno
        csv_writer.writerow([
            alumno.dni,
            alumno.nombre,
            alumno.apellido,
            alumno.telefono,
            alumno.correo_electronico,
            alumno.curso.nombre if alumno.curso else '',  # Asegurarse de manejar el caso de curso nulo
            alumno.banda_horaria.nombre if alumno.banda_horaria else '',  # Asegurarse de manejar el caso de banda horaria nula
        ])

        return response

def modificar_alumno(request, dni):
    #el método PUT se utiliza para actualizar un recurso existente.
    if request.method == 'PUT':
        try:
            #la función utiliza json.loads(request.body) para analizar el cuerpo JSON de la solicitud
            data = json.loads(request.body) 
            #se utiliza "get_object_or_404" para obtener el objeto Alumno con el DNI proporcionado. 
            #si no se encuentra un alumno con ese DNI, se devuelve un error 404 No encontrado.

            alumno = get_object_or_404(Alumno, dni=dni)

            # Crear un objeto de respuesta HTTP con el tipo de contenido CSV
            response = HttpResponse(content_type='text/csv')

            # Establecer el encabezado para la descarga del archivo
            response['Content-Disposition'] = f'attachment; filename=alumno_modificado_{alumno.dni}.csv'

            # Crear un escritor CSV usando el objeto de respuesta como destino
            csv_writer = csv.writer(response)

            # Escribir las filas de datos actualizados del alumno
            csv_writer.writerow(['DNI', 'Nombre', 'Apellido', 'Teléfono', 'Correo Electrónico', 'Curso'])
            csv_writer.writerow([alumno.dni, data.get('nombre', alumno.nombre), data.get('apellido', alumno.apellido), 
                                data.get('telefono', alumno.telefono), data.get('correo_electronico', alumno.correo_electronico), 
                                data.get('curso', alumno.curso.nombre if alumno.curso else 'N/A')])

            # Actualizar los datos del alumno con los nuevos valores
            for key, value in data.items():
                #se utiliza "setattr" para actualizar dinámicamente los atributos del objeto Alumno con los nuevos valores.
                setattr(alumno, key, value)
            alumno.save()

            return response

        except Exception as e:
            # Devuelve un mensaje de error si hay algún problema durante el proceso
            return HttpResponse(f'Error: {str(e)}', status=500)
    else:
        # Devuelve un código de estado 405 (Method Not Allowed) si se utiliza un método no permitido
        return HttpResponseNotAllowed(['PUT'])



def eliminar_alumno(request, dni):
    if request.method == 'DELETE':
        try:
            alumno = get_object_or_404(Alumno, dni=dni)

            # Crear un objeto de respuesta HTTP con el tipo de contenido CSV
            response = HttpResponse(content_type='text/csv')

            # Establecer el encabezado para la descarga del archivo
            response['Content-Disposition'] = f'attachment; filename=alumno_eliminado_{alumno.dni}.csv'

            # Crear un escritor CSV usando el objeto de respuesta como destino
            csv_writer = csv.writer(response)

            # Escribir las filas de datos del alumno
            csv_writer.writerow(['DNI', 'Nombre', 'Apellido', 'Teléfono', 'Correo Electrónico', 'Curso'])
            csv_writer.writerow([alumno.dni, alumno.nombre, alumno.apellido, alumno.telefono, alumno.correo_electronico, alumno.curso.nombre if alumno.curso else 'N/A'])

            # Eliminar al alumno después de escribir la información en CSV
            alumno.delete()

            return response

        except Exception as e:
            # Devuelve un mensaje de error si hay algún problema durante el proceso
            return HttpResponse(f'Error: {str(e)}', status=500)
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

            # Crear un objeto de respuesta HTTP con el tipo de contenido CSV
            response = HttpResponse(content_type='text/csv')
            
            # Establecer el encabezado para la descarga del archivo
            response['Content-Disposition'] = f'attachment; filename=curso_asignado_{alumno.dni}.csv'

            # Crear un escritor CSV usando el objeto de respuesta como destino
            csv_writer = csv.writer(response)

            # Escribir las filas de datos del alumno
            csv_writer.writerow(['DNI', 'Nombre', 'Curso Asignado'])
            csv_writer.writerow([alumno.dni, alumno.nombre, curso.nombre])

            return response

        except Exception as e:
            # Devuelve un mensaje de error si hay algún problema durante el proceso
            return HttpResponse(f'Error: {str(e)}', status=500)
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
            
            # Crear un objeto de respuesta HTTP con el tipo de contenido CSV
            response = HttpResponse(content_type='text/csv')
            
            # Establecer el encabezado para la descarga del archivo
            response['Content-Disposition'] = f'attachment; filename=alumnos_curso_{curso.id}.csv'

            # Crear un escritor CSV usando el objeto de respuesta como destino
            csv_writer = csv.writer(response)

            # Escribir la fila de encabezado
            csv_writer.writerow(['DNI', 'Nombre'])

            # Escribir las filas de datos de los alumnos
            for alumno in alumnos:
                csv_writer.writerow([alumno.dni, alumno.nombre])

            return response

        except Exception as e:
            # Devuelve un mensaje de error si hay algún problema durante el proceso
            return HttpResponse(f'Error: {str(e)}', status=500)
    else:
        # Devuelve un código de estado 405 (Method Not Allowed) si se utiliza un método no permitido
        return HttpResponseNotAllowed(['GET'])
