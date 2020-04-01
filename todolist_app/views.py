from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
	if request.method == "POST":
		form = TaskForm(request.POST or None)
		if form.is_valid():
			form.save(commit=False).manage = request.user #we are using this to associate a created task to particular user 
			form.save()
		messages.success(request, ("New Task Added"))
		return redirect("todolist") #here we are giving view function name "todolist"
	else:	
		# all_tasks = TaskList.objects.all #earlier we were using this to access all task but we have update this in next line to particular user
		all_tasks = TaskList.objects.filter(manage=request.user)
		return render(request, 'todolist.html', {'all_tasks': all_tasks}) 
	# context = {
	# 'welcome_text':"Welcome to todo list",
	# }
	# return render(request, 'todolist.html', context) #this is to display the content of "todolist.html" file
	# return HttpResponse("Welcome to todolist app page") #this is to just display some text

def deleteTask(request, task_id):
	task = TaskList.objects.get(pk=task_id)
	task.delete()
	return redirect("todolist")

def editTask(request, task_id):
	if request.method == "POST":
		task = TaskList.objects.get(pk=task_id)
		form = TaskForm(request.POST or None, instance=task)
		if form.is_valid():
			form.save()
		return redirect("todolist") #here we are giving view function name "todolist"
	else:	
		edit_task = TaskList.objects.get(pk=task_id)
		return render(request, 'edit.html', {'edit_task': edit_task})

def completeTask(request, task_id):
	task = TaskList.objects.get(pk=task_id)
	task.done = True
	task.save()
	return redirect("todolist")

def pendingTask(request, task_id):
	task = TaskList.objects.get(pk=task_id)
	task.done = False
	task.save()
	return redirect("todolist")

def index(request):
	context = {
	'index_text':"Welcome to Todolist home page",
	}
	return render(request, 'index.html', context)

def contact(request):
	context = {
	'contact_text':"Welcome to contact us page",
	}
	return render(request, 'contact.html', context)

def about(request):
	context = {
	'about_text':"Welcome to about us page",
	}
	return render(request, 'about.html', context)