from django.shortcuts import render
from todos.models import Task

def home(request):
    incompleted_tasks = Task.objects.filter(is_completed=False).order_by('-update_at')
    completed_tasks = Task.objects.filter(is_completed=True)
    context = {
        'incompleted_tasks' : incompleted_tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request,'index.html', context)