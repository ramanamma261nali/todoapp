from django.shortcuts import render

from todo.models import Task



def home1(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_tasks=Task.objects.filter(is_completed=True)
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request,'home1.html',context)
    