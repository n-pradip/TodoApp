from django.shortcuts import render,redirect
from main_app.models import Todo
from main_app.forms import TodoForm

def todoList(request):
    all_list = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        obj = TodoForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/')
    context = {
        'all_list':all_list,
        'form':form
    }
    return render(request,'index.html',context)

def update_todo(request,pk):
    obj = Todo.objects.get(id=pk)
    form = TodoForm(instance=obj)
    if request.method == 'POST':
        obj = TodoForm(request.POST, instance=obj)
        if obj.is_valid():
         obj.save()
         return redirect('/')
    context={
        'form':form
    }
    return render(request,'update_todo.html',context)

def delete_todo(request,pk):
    obj = Todo.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    context = {
        'data':obj
    }   
    return render(request,'confirm_del.html',context)

