from django.utils import timezone
from gestion_alumno.models import Curso, BandaHoraria, Alumno

# Crear bandas horarias
banda_horaria1 = BandaHoraria.objects.create(nombre="Mañana", horario_inicio=timezone.now(), horario_fin=timezone.now())
banda_horaria2 = BandaHoraria.objects.create(nombre="Tarde", horario_inicio=timezone.now(), horario_fin=timezone.now())

# Crear cursos
curso1 = Curso.objects.create(nombre="Curso de Matemáticas", descripcion="Curso avanzado de matemáticas", nota=80, banda_horaria=banda_horaria1)
curso2 = Curso.objects.create(nombre="Curso de Historia", descripcion="Curso introductorio de historia", nota=75, banda_horaria=banda_horaria2)

# Crear alumnos
alumno1 = Alumno.objects.create(nombre="Juan", apellido="Pérez", dni=12345678, telefono="123-456-7890", correo_electronico="juan@example.com", curso=curso1)
alumno2 = Alumno.objects.create(nombre="Ana", apellido="Gómez", dni=23456789, telefono="987-654-3210", correo_electronico="ana@example.com", curso=curso2)
alumno3 = Alumno.objects.create(nombre="Carlos", apellido="López", dni=34567890, telefono="555-123-4567", correo_electronico="carlos@example.com", curso=curso1)

print("Datos de ejemplo creados exitosamente.")
