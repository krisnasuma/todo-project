from multiprocessing import context
from sys import exec_prefix
from urllib import request

from django.shortcuts import render, redirect


from django.contrib import messages

from django.http import HttpResponse #if used httpresponse, then we can import HttpResponse from django.http
from django.http import Http404

#import class task from todo/models.py
from .models import Task
#import class task from todo/forms.py
from .forms import TaskForm

# Create your views here.

#show database page
def my_viewss(request): 
    #return HttpResponse("Welcome Ya") #use the HttpResponse class to return a response, if used HttpResponse, then we can import HttpResponse

    #get all the tasks from the models/database
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    #pharse task data to template todo/index.html and render it
    return render(request, 'todo/index.html', context)


#make view page for "detail page"
def detail_view(request, task_id):
    #get data from task wihout task_id
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        #if task data not found, then raise/redirect code 404 (page not found)
        raise Http404("Task Not Found.")
    #pharsing task data to template todo/detail.html and render it
    return render(request, 'todo/detail.html', context)

#make view page for "create form" with widget-tweaks
def create_view(request):
    #check method in request
    #if method is POST, then request processing will be run
    #run validation process and save data to database
    if request.method == 'POST':
        #create object from class TaskForm
        new_task  = TaskForm(request.POST)
        #check validation form process
        if new_task.is_valid():
            # Save data into the tasks table
            new_task.save()
            # set success message and redirect to task list page
            messages.success(request, 'Success.')
            return redirect('todo:index')

    #if method is not POST
    else:
        # create an object from the TaskForm class
        form = TaskForm()
        args = {'form': form}
        
        #render form template by parsing form data   
        return render(request, 'todo/form.html', args)

#create view for edit page function
def update_view(request, task_id):
    try:
        #get task based from task_id
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        #if data not found, else will be redirect to page 404 (not found)
        raise Http404("Task Not Found.")
    #check method request
    #if method is post, then system will be execute
    # to validate and saved data
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            #save changed to table tasks
            form.save()
            #set success messages and redirect to task list
            messages.success(request, 'Data Changed.')
            return redirect('todo:index')
    
    #if method is'nt POST
    else:
        #create object from TaskForm class
        form=TaskForm(instance=task)
        #render template with pharse data method from form
        return render(request, 'todo/form.html', {'form': form})

#create delete function
def delete_view(request, task_id):
    try:
        #get task data will be delete based on task id
        task = Task.objects.get(pk=task_id)
        #delete data form task table
        task.delete()
        #set success messages and redirect to task list
        messages.success(request, 'Delete Success.')
        return redirect('todo:index')
    except Task.DoesNotExist:
        #if data not Found
        #then will be redirect to 404 page (Page Not Found)
        raise Http404("Task Not Found.")
