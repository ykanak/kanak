from django.shortcuts import render, HttpResponse, redirect
from home.models import task
# Create your views here.
def home(request):
    context = {'success':False}
    if request.method =="POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = task(taskTitle=title , taskDisc=desc)
        ins.save()
        context = {'success':True}
        

    return render(request, 'index.html', context)

def tasks(request):
    allTasks = task.objects.all()
        # print(allTasks)
        # for item in allTasks:
        #     print(item.taskTitle)
    context = {'tasks':allTasks}
    return render(request, 'tasks.html', context) 

def deleteTask(request, pk):
    delTask = task.objects.get(id=pk)
    if request.method == "POST":
        delTask.delete()
        return redirect('/')
    context = {'item':delTask}
    return render(request, 'deleteTask.html', context)       