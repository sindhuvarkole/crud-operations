from django.shortcuts import render

from app.models import Student


def abc(request):
    data=Student.object.all()
    context={"data":data}
    return render(request,"index.html")

def update(request,id):
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def about(request):
    return render(request,"about.html")

