from django.shortcuts import render, redirect
from .models import Mascota, Cita, Cliente, MedicoVeterinario
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def crear_usuario(request):
    return render(request, 'crear_usuario.html')


def ingresar_usuario(request):
        cliente = Cliente(nombre = request.POST['nombre'],
                      apellido = request.POST['apellido'],
                      rut= request.POST['rut'],
                      telefono=request.POST['telefono'],
                      correo= request.POST['correo'],
                      direccion= request.POST['direccion'],
                      password=request.POST['password'])
        cliente.save()
        return render(request,'index.html')



def interfaz(request):
    citas = Cita.objects.all()
    mascotas = Mascota.objects.all()
    veterinarios = MedicoVeterinario.objects.all()

    
    return render(request, 'interfaz.html',{'mascotas': mascotas,'veterinarios': veterinarios,'citas':citas, 'veterinarios': veterinarios,'cliente':request.session['cliente']})

def login(request):
    mascotas = Mascota.objects.all()
    veterinarios = MedicoVeterinario.objects.all()
    citas = Cita.objects.all()
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        
        try:
            cliente = Cliente.objects.get(correo=correo, password=password)
            
        
        except Cliente.DoesNotExist:
          
            return redirect('/')
        

    request.session['cliente'] = {
            'id': cliente.id,
            'nombre': cliente.nombre,
            'correo': cliente.correo,
        }
    
    cliente1 = Cliente.objects.get(id=cliente.id)
   
    return render(request,'interfaz.html',{'mascotas': mascotas, 'veterinarios': veterinarios,'cliente':cliente1,'citas': citas})




def eliminar(request,id_m):
    
    mascota = Mascota.objects.get(id = id_m)
    mascota.delete()
        
    return redirect('/interfaz')


def guardar_mascota(request):
   
    if request.method == 'POST':
        nombre = request.POST.get('nombre_mascota')
        especie = request.POST.get('especie_mascota')
        raza = request.POST.get('raza_mascota')
        sexo = request.POST.get('sexo_mascota')
        edad = request.POST.get('edad_mascota')
        peso = request.POST.get('peso_mascota')

        nueva_mascota = Mascota(nombre=nombre, especie=especie, raza=raza, sexo=sexo, edad=edad, peso=peso)
        nueva_mascota.save()

        return redirect('/interfaz')  # Redirecciona a la página principal después de guardar
    else:
        return render(request, 'interfaz.html')

def guardar_cita(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        mascota_id = request.POST.get('mascota')
        medico_id = request.POST.get('medico')
        fecha_formulario = request.POST.get('fecha')
        hora = request.POST.get('hora')
        motivo = request.POST.get('motivo')

        # Verificar si la fecha_entrada no es None y no está vacía
        fecha_entrada = datetime.strptime(fecha_formulario, '%d/%m/%y').strftime('%Y-%m-%d')
        nueva_cita = Cita(cliente_id=cliente_id, mascota_id=mascota_id, medico_id=medico_id, fecha=fecha_entrada, hora=hora, motivo=motivo)
        nueva_cita.save()

        return redirect('interfaz')  # Redirecciona a la página principal después de guardar

    # Obtener todas las mascotas de la base de datos
    mascotas = Mascota.objects.all()
    return render(request, 'interfaz.html', {'mascotas': mascotas})


def ver_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'interfaz.html', {'mascotas': mascotas})

def actualizar(request, id_m):
    try:
        editar_mascota = Mascota.objects.get(id=id_m)
    except Mascota.DoesNotExist:
        return render(request, 'error.html', {'mensaje': 'La mascota no existe.'})
    if request.method == 'GET':
        return render(request, 'editar_mascota.html', {'mascota': editar_mascota})
    if request.method == 'POST':
        editar_mascota.nombre = request.POST.get('nombre', editar_mascota.nombre)
        editar_mascota.especie = request.POST.get('especie', editar_mascota.especie)
        editar_mascota.raza = request.POST.get('raza', editar_mascota.raza)
        editar_mascota.sexo = request.POST.get('sexo', editar_mascota.sexo)
        editar_mascota.peso = request.POST.get('peso', editar_mascota.peso)
        editar_mascota.edad = request.POST.get('edad', editar_mascota.edad)
        editar_mascota.save()
        return redirect('/interfaz')
    return render(request, 'interfaz.html')

def logout(request):
    try:
        del request.session['cliente']
    except KeyError:
       print('error')
    return redirect('/')


