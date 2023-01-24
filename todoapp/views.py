from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie
def index(request):
    form = TaskForm()
    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    tasks = Task.objects.all()
    return render(request, "index.html", {"task_form": form, "tasks": tasks})


@ensure_csrf_cookie
def update_task(request, pk):
    # pk -> primary key
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "update_task.html", {"task_edit_form": form})


@ensure_csrf_cookie
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")
