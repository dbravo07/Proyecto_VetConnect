from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('interfaz/', views.interfaz, name='interfaz'),
    path('crear_usuario/', views.crear_usuario,name='crear_usuario'),
    path('login/', views.login ),
    path('comprobacion/', views.ingresar_usuario),
    path('eliminar/<id_m>/',views.eliminar),
    path('actualizar/<int:id_m>/', views.actualizar, name='actualizar'),
    path('guardar_mascota/', views.guardar_mascota, name='guardar_mascota'),
    path('guardar_cita/<int:cliente_id>/', views.guardar_cita, name='guardar_cita'),
    path('guardar_cita/', views.guardar_cita, name='guardar_cita'),
    path('ver_mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('cerrar_sesion/',views.logout)


    ]
