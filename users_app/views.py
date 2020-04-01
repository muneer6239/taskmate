from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm      #initially we were using this form but now we are using "CustomRegisForm"
from users_app.forms import CustomRegisForm
from django.contrib import messages

# Create your views here.
def registeration(request):
	if request.method == "POST":
		register_form = CustomRegisForm(request.POST)
		# register_form = UserCreationForm(request.POST) #initially we were using this form but now we are using "CustomRegisForm"
		if register_form.is_valid():
			register_form.save()
			messages.success(request, ("User Account Created"))
		return redirect("registeration")
	else:
		register_form = CustomRegisForm()
		# register_form = UserCreationForm() #initially we were using this form but now we are using "CustomRegisForm"
		return render(request,"register.html", {"register_form":register_form})
	# return HttpResponse("usersapp is working") #we were printing text only first but now using "register.html" file for output