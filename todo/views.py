from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.

@login_required(login_url="/login/")
def TodoIndex(request):
    context = {}
    if request.method == "POST":
        if request.POST["name"] != "" and request.POST["email"] != "":
            name = request.POST["name"]
            email = request.POST["email"]
            group = request.POST["group"]

            student = Student()
            student.name = name
            student.email = email
            student.group = group

            student.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        context = {}
        students = Student.objects.all().order_by('-id')
        return render(request, 'todo/index.html', locals())

@login_required(login_url="/login/")
def TodoDelete(request, student_id):
    Student.objects.get(id=student_id).delete()
    return redirect('/')

@login_required(login_url="/login/")
def TodoUpdate(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(id=student_id)
        student.name = request.POST["name"]
        student.email = request.POST["email"]
        student.group = request.POST["group"]
        student.save()
        return redirect('/')
    else:
        student = Student.objects.get(id=student_id)
        return render(request, 'todo/update.html', locals())


def TodoLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            students = Student.objects.all().order_by('-id')
            return render(request, 'todo/index.html', locals())
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def TodoLogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')