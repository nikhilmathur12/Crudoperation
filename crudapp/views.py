from django.shortcuts import render, redirect
from .models import Data
from .form import DataForm


# Create your views here.
def home(request):
    datas = Data.objects.all()
    context = {
        "datas": datas
    }
    return render(request, "home.html", context)


def create(request):
    form = DataForm()
    if request.method == "POST":
        form = DataForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    context = {
        "form": form
    }
    return render(request, "create.html", context)


def update(request, pk):
    updates = Data.objects.get(id=pk)
    form = DataForm(instance=updates)
    if request.method == "POST":
        form = DataForm(request.POST, instance=updates)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "form": form
    }
    return render(request, "create.html", context)


def delete(request, pk):
    deletes = Data.objects.get(id=pk)
    if request.method == "POST":
        deletes.delete()
        return redirect("home")
    context = {
        "item": deletes
    }
    return render(request, "delete.html", context)
