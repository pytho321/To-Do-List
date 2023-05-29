from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'create_task.html')

def delete(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    tasks.delete()
    return redirect('task_list')
    



