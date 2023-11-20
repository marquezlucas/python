from django.urls import path
#from .views import cargar_alumnos, listar_alumnos, obtener_alumno, modificar_alumno, eliminar_alumno, asignar_curso, alumnos_por_curso
from . import views
urlpatterns = [
    path('cargarAlumnos/', views.cargar_alumnos, name='cargar_alumnos'),
    path('listarAlumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('alumno/<str:dni>/', views.obtener_alumno, name='obtener_alumno'),
    path('modificarAlumno/<str:dni>/', views.modificar_alumno, name='modificar_alumno'),
    path('eliminarAlumno/<str:dni>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('asignarCurso/<str:dni>/<int:id_curso>/', views.asignar_curso, name='asignar_curso'),
    path('alumnosPorCurso/<int:id_curso>/', views.alumnos_por_curso, name='alumnos_por_curso'),
]

""" path('cargar_alumnos/', cargar_alumnos, name='cargar_alumnos'),
    path('listar_alumnos/', listar_alumnos, name='listar_alumnos'),
    path('alumno/<str:dni>/', obtener_alumno, name='obtener_alumno'),
    path('modificar_alumno/<str:dni>/', modificar_alumno, name='modificar_alumno'),
    path('eliminar_alumno/<str:dni>/', eliminar_alumno, name='eliminar_alumno'),
    path('asignar_curso/<str:dni>/<int:id_curso>/', asignar_curso, name='asignar_curso'),
    path('alumnos_por_curso/<int:id_curso>/', alumnos_por_curso, name='alumnos_por_curso'),"""