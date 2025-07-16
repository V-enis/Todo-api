from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm

def todo_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = PostForm()
    todos = Todo.objects.order_by('created_date')
    return render(request, 'todo_list.html', {'todos': todos, 'form': form})


def toggle_status(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if todo.completed == True:
        todo.completed = False
        todo.save()
        return redirect('todo_list')
    else:
        todo.completed = True
        todo.save()
        return redirect('todo_list')

def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = PostForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')


# Create your views here.
