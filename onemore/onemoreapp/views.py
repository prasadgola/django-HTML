from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from onemoreapp.models import Gola,Person,users,onetoone, weeklypresentation
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

def ppl(request):
	if request.method == "POST":
		if request.POST['name'] and request.POST['image']:
			post = Person()
			post.first_nam = request.POST['name']
			post.last_nam = request.POST['image']
			print(post.first_nam)
			post.save()
			user = authenticate(request, username=post.first_nam,password=post.last_nam)
			if user:
				login(request, user)
				return HttpResponseRedirect(reverse('user_success'))
			else:
				return render(request,"index.html")
	else:
		return render(request,"index.html")







def user_login(request):
	if request.method == "POST":
		basava = Gola()
		basava.first_nam= request.POST['username']
		basava.last_nam = request.POST['password']
		basava.save()
		print(basava.first_nam)
		print(basava.last_nam)
		user = authenticate(request, username=basava.first_nam,password=basava.last_nam)
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse('user_success'))
		else:
			return render(request,"login.html")
	else:
		return render(request,"login.html")
		

# def show(request):
# 	people = Person.objects.all()
# 	return render(request,"show.html",{'ppl':people})



def signup(request):
	if request.method == "POST":
		register = users()
		register.firstname = request.POST['firstname']
		register.lastname = request.POST['lastname']
		register.birthday = request.POST['birthday']
		register.gender = request.POST['gender']
		register.phonenumber = request.POST['phonenumber']
		register.specialization = request.POST['stream']
		register.username = request.POST['email']
		register.password = request.POST['password']
		register.image = request.POST['image']
		register.save()
		user = User.objects.create_user(register.username,register.username,register.password)
		user.save()
		return HttpResponseRedirect(reverse('signin'))
	return render(request,"signup.html")




def signin(request):	
	if request.method == "POST":
		username = request.POST['userconnected']
		password = request.POST['passwordconnected']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('jvtconnect'))
		else:
			return HttpResponseRedirect(reverse('signin'))
	return render(request,"signin.html")

def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse('signin'))

def jvtconnect(request):
	return render(request,"connect.html")



def one2one(request):
	if request.method == "POST":
		one2one = onetoone()
		one2one.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		one2one.partner = request.POST['partner']
		one2one.onetopic = request.POST['Topic']
		one2one.oneduration = request.POST['Time']
		one2one.onedate = request.POST['Date']
		one2one.save()
		return HttpResponseRedirect('jvtconnect')


def weeklypre(request):
	if request.method == "POST":
		week = weeklypresentation()
		week.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		week.weektopic= request.POST['Topicname']
		week.weekduration= request.POST['Time']
		week.weekdate= request.POST['Date']
		week.save()
		return HttpResponseRedirect('jvtconnect')



# def (request):
# 	if request.method == "POST":
# 		.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
# 		.save()
# 		return HttpResponseRedirect('jvtconnect')



# def (request):
# 	if request.method == "POST":
# 		.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
# 		.save()
# 		return HttpResponseRedirect('jvtconnect')


# def (request):
# 	if request.method == "POST":
# 		.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
# 		.save()
# 		return HttpResponseRedirect('jvtconnect')


# def (request):
# 	if request.method == "POST":
# 		.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
# 		.save()
# 		return HttpResponseRedirect('jvtconnect')


# def (request):
# 	if request.method == "POST":
# 		.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
# 		.save()
# 		return HttpResponseRedirect('jvtconnect')






