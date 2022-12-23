from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import pedidoForm
from .models import Pedidos
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect('pedidos')
            except:
                return render(request,"signup.html",{
                     "form": UserCreationForm,
                     "error": "El usuario ya existe"
                     })
        return render(request,'signup.html',{
            'form':UserCreationForm, 
            'error': "Las contraseñas no coinciden"
            })

@login_required
def pedidos(request):
    pedido = Pedidos.objects.filter(user=request.user)
    return render(request, 'pedidos.html',{'pedidos': pedido})

 
@login_required           
def crear_pedidos(request):
    if request.method == 'GET':
        return render(request, 'crear_pedidos.html',{
            'form': pedidoForm,
            'titulo': 'Crear'
        })
    else:
        try:
            form = pedidoForm(request.POST)
            nuevo_pedido = form.save(commit=False)
            nuevo_pedido.user = request.user
            nuevo_pedido.save()
            return redirect('pedidos')
        except:
            return render(request,'crear_pedidos.html',{
                'form': pedidoForm,
                'error': 'Ingrese datos validos',
                'titulo': 'Crear'
            })
        
 
@login_required
def detalle_pedidos(request, id):
    if request.method == "GET":
        pedido = get_object_or_404(Pedidos, id=id)
        form = pedidoForm(instance=pedido)
        return render(request,'detalle_pedidos.html',{
            'pedido':pedido,
            'form':form,
            'titulo': 'editar'
        })
    else:
        try:
            pedido = get_object_or_404(Pedidos, id=id)
            form = pedidoForm(request.POST, instance=pedido)
            form.save()
            return redirect('pedidos')
        except:
            return render(request, 'detalle_pedidos.html',{
                'pedido':pedido,
                'form':form,
                'error':'Error al actualizar la tarea',
                'titulo': 'editar'
            })

def eliminarPedido(request,id):
    pedido = Pedidos.objects.get(id=id)
    pedido.delete()
    return redirect('/pedidos')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("index")

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signup.html',{
                'form': AuthenticationForm,
                'error': 'Nombre de usuario o contraseña incorrectos'
            })
        login(request, user)
        return redirect('pedidos')