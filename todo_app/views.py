from django.shortcuts import render, redirect
from .models import Todo
from .forms import task_form

def tasks(request):
    html = 'todo_app/app.html'
    tasks = Todo.objects.all()
    form = task_form()
    form_del = None
    if 'del' in request.POST:
        form_del = Todo.objects.get(id = request.POST['del'])
    if request.method == 'POST':
        if 'del' in request.POST:
            form_del.delete()
            return redirect('tasks')
        if 'add' in request.POST:
            form = task_form(request.POST)
            form.save()
            return redirect('tasks')

    context = {'tasks':tasks,
               'form':form,
               'form_del':form_del
               }
    
    return render(request,html,context)
