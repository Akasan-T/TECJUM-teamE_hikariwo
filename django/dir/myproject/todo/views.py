from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-priority', 'due_date')
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    # task_create で完了・未完了のタスクをコンテキストに入れている場合（必要なら）
    completed_tasks = Task.objects.filter(user=request.user, completed=True)
    incomplete_tasks = Task.objects.filter(user=request.user, completed=False)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo:task_list')
    else:
        form = TaskForm()
    
    # コンテキストを1つの辞書にまとめる
    context = {
        'form': form,
        'completed_tasks': completed_tasks,
        'incomplete_tasks': incomplete_tasks,
    }
    return render(request, 'task_form.html', context)

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('todo:task_list')
