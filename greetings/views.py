from django.shortcuts import render, redirect
from .models import Person

def enter_name(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            person = Person.objects.create(name=name)
            return redirect("hello", person_id=person.id)
    return render(request, "enter_name.html")

def hello_name(request, person_id):
    person = Person.objects.get(id=person_id)
    return render(request, "hello.html", {"name": person.name})

# 10.32.106.4