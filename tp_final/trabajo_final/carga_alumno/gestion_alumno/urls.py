from django.urls import path
#from .views import cargar_alumnos, listar_alumnos, obtener_alumno, modificar_alumno, eliminar_alumno, asignar_curso, alumnos_por_curso
from . import views

urlpatterns = [
    path('', views.cargar_alumnos, name='cargar_alumnos'),
    path('', views.listar_alumnos, name='listar_alumnos'),
    path('', views.obtener_alumno, name='obtener_alumno'),
    path('', views.modificar_alumno, name='modificar_alumno'),
    path('', views.eliminar_alumno, name='eliminar_alumno'),
    path('', views.asignar_curso, name='asignar_curso'),
    path('', views.alumnos_por_curso, name='alumnos_por_curso'),
]


"""
urlpatterns = [
    path('cargarAlumnos/', cargar_alumnos, name='cargar_alumnos'),
    path('listarAlumnos/', listar_alumnos, name='listar_alumnos'),
    path('alumno/<str:dni>/', obtener_alumno, name='obtener_alumno'),
    path('modificarAlumno/<str:dni>/', modificar_alumno, name='modificar_alumno'),
    path('eliminarAlumno/<str:dni>/', eliminar_alumno, name='eliminar_alumno'),
    path('asignarCurso/<str:dni>/<int:id_curso>/', asignar_curso, name='asignar_curso'),
    path('alumnosPorCurso/<int:id_curso>/', alumnos_por_curso, name='alumnos_por_curso'),
]
"""
"""
urlpatterns = [
    path('cargarAlumnos/', views.cargar_alumnos, name='cargar_alumnos'),
    path('listarAlumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('alumno/<str:dni>/', views.obtener_alumno, name='obtener_alumno'),
    path('modificarAlumno/<str:dni>/', views.modificar_alumno, name='modificar_alumno'),
    path('eliminarAlumno/<str:dni>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('asignarCurso/<str:dni>/<int:id_curso>/', views.asignar_curso, name='asignar_curso'),
    path('alumnosPorCurso/<int:id_curso>/', views.alumnos_por_curso, name='alumnos_por_curso'),
]
"""