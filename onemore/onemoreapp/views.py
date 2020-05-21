from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from onemoreapp.models import Gola,Person,users,onetoone, weeklypresentation, dailypresentation, socials, visitors, referralsgiven, referralstaken
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
		



def signup(request):
	if request.method == "POST" and request.FILES:
		register = users()
		register.firstname = request.POST['firstname']
		register.lastname = request.POST['lastname']
		register.birthday = request.POST['birthday']
		register.gender = request.POST['gender']
		register.phonenumber = request.POST['phonenumber']
		register.specialization = request.POST['stream']
		register.username = request.POST['email']
		register.password = request.POST['Password']
		register.image = request.FILES['image']
		register.address = request.POST['address']
		register.city = request.POST['city']
		register.course = request.POST['Course']
		register.pincode = request.POST['pincode']
		register.save()
		user = User.objects.create_user(register.username,register.username,register.password)
		user.save()
		return HttpResponseRedirect(reverse('signin'))
	return render(request,"signup.html")




def signin(request):
	context = {}
	if request.method == "POST":
		username = request.POST['userconnected']
		password = request.POST['passwordconnected']
		user = authenticate(request, username = username, password = password)
		if user is not None:

			login(request, user)
			if username == 'pawan123456@gmail.com':
				return HttpResponseRedirect(reverse('adminpage'))
			else:
				return HttpResponseRedirect(reverse('jvtconnect'))
		else:
			context['a'] = 'a'
	return render(request,"signin.html",context)

def signout(request):
	logout(request)
	return HttpResponseRedirect(reverse('signin'))

def jvtconnect(request):
	details = users.objects.get(user_id = request.user.id)
	employee = users.objects.all()
	content = {
	'details' : details,
	'employee' : employee
	}
	return render(request,"jvtconnect.html",content)

def adminpage(request):
	u = users.objects.all()
	context = { 'u' : u }
	if request.method == "POST":
		employeeid = request.POST['userid']
		request.session['employee_id_sess'] = employeeid
		return HttpResponseRedirect(reverse('viewreport'))
	return render(request,"adminpage.html",context)

def viewreport(request):
	return render(request,"viewreport.html")



def one2one(request):
	if request.method == "POST":
		one2one = onetoone()
		one2one.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		one2one.onemet = request.POST['Met']
		one2one.onelocation = request.POST['Loc']
		one2one.onetopic = request.POST['Topic']
		# one2one.oneduration = request.POST['Time']
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



def dailypre(request):
	if request.method == "POST":
		daily = dailypresentation()
		daily.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		daily.dailytopic = request.POST['Topic']
		daily.dailyduration = request.POST['Time']
		daily.dailydate = request.POST['Date']
		daily.save()
		return HttpResponseRedirect('jvtconnect')



def social(request):
	if request.method == "POST":
		social_s = socials()
		social_s.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		social_s.socialstopic = request.POST['Topicname']
		social_s.socialsduration = request.POST['Time']
		social_s.socialsdate = request.POST['Date']
		social_s.save()
		return HttpResponseRedirect('jvtconnect')


def visitor(request):
	if request.method == "POST":
		visitor_s = visitors()
		visitor_s.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		visitor_s.visitorstopic = request.POST['Topicname']
		visitor_s.visitorsduration = request.POST['Time']
		visitor_s.visitorsdate = request.POST['Date']
		visitor_s.save()
		return HttpResponseRedirect('jvtconnect')


def given(request):
	if request.method == "POST":
		give = referralsgiven()
		give.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		give.giventopic = request.POST['Topicname']
		give.givenduration = request.POST['Time']
		give.givendate = request.POST['Date']
		give.save()
		return HttpResponseRedirect('jvtconnect')


def taken(request):
	if request.method == "POST":
		take = referralstaken()
		take.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		take.takentopic = request.POST['Topicname']
		take.takenduration = request.POST['Time']
		take.takendate = request.POST['Date']
		take.save()
		return HttpResponseRedirect('jvtconnect')




def onetooneview(request):
	admin_userid = request.session.get('employee_id_sess', None)
	o = onetoone.objects.raw(f'select onetooneid from onemoreapp_onetoone where user_id = {request.user.id}') or onetoone.objects.raw(f'select onetooneid from onemoreapp_onetoone where user_id = {admin_userid}')
	context = {'o' : o}
	return render(request,"onetooneview.html",context)

def dailyview(request):
	admin_userid = request.session.get('employee_id_sess', None)
	d = dailypresentation.objects.raw(f'select dailypresentationid from onemoreapp_dailypresentation where user_id = {request.user.id}') or dailypresentation.objects.raw(f'select dailypresentationid from onemoreapp_dailypresentation where user_id = {admin_userid}')
	context = {'d' : d}
	return render(request,"dailyview.html",context)

def weeklyview(request):
	admin_userid = request.session.get('employee_id_sess', None)
	w = weeklypresentation.objects.raw(f'select weeklypresentationid from onemoreapp_weeklypresentation where user_id = {request.user.id}') or weeklypresentation.objects.raw(f'select weeklypresentationid from onemoreapp_weeklypresentation where user_id = {admin_userid}')
	context = {'w' : w}
	return render(request,"weeklyview.html",context)

def socialsview(request):
	admin_userid = request.session.get('employee_id_sess', None)
	s = socials.objects.raw(f'select socialsid from onemoreapp_socials where user_id = {request.user.id}') or socials.objects.raw(f'select socialsid from onemoreapp_socials where user_id = {admin_userid}')
	context = {'s' : s}
	return render(request,"socialsview.html",context)

def visitorsview(request):
	admin_userid = request.session.get('employee_id_sess', None)
	v = visitors.objects.raw(f'select visitorsid from onemoreapp_visitors where user_id = {request.user.id}') or visitors.objects.raw(f'select visitorsid from onemoreapp_visitors where user_id = {admin_userid}')
	context = {'v' : v}
	return render(request,"visitorsview.html",context)

def referralsgivenview(request):
	admin_userid = request.session.get('employee_id_sess', None)
	rg = referralsgiven.objects.raw(f'select referralsgivenid from onemoreapp_referralsgiven where user_id = {request.user.id}') or referralsgiven.objects.raw(f'select referralsgivenid from onemoreapp_referralsgiven where user_id = {admin_userid}')
	context = {'rg' : rg}
	return render(request,"referralsgivenview.html",context)

def referralstakenview(request):
	admin_userid = request.session.get('employee_id_sess', None)
	rt = referralstaken.objects.raw(f'select referralstakenid from onemoreapp_referralstaken where user_id = {request.user.id}') or referralstaken.objects.raw(f'select referralstakenid from onemoreapp_referralstaken where user_id = {admin_userid}')
	context = {'rt' : rt}
	return render(request,"referralstakenview.html",context)

	


def profile(request):
	p = users.objects.get(user_id = request.user.id)
	context = {'p' : p}
	return render(request,"profile.html",context)

def edit(request):
	details = users.objects.get(user_id = request.user.id)
	content = {
		'username' : details.username,
		'password' : details.password,
		'firstname' : details.firstname,
		'lastname' : details.lastname,
		'birthday' : details.birthday,
		'gender' : details.gender,
		'phonenumber' : details.phonenumber,
		'specialization' : details.specialization,
		'image' : details.image.url,
	}	

	
	if request.method == "POST" and request.FILES:
		details.username = request.POST['email']
		details.password = request.POST['password']
		details.firstname = request.POST['firstname']
		details.lastname = request.POST['lastname'] 
		details.birthday = request.POST['birthday']
		details.gender = request.POST['gender']
		details.phonenumber = request.POST['phonenumber']
		details.specialization = request.POST['stream']
		details.image = request.FILES['image']
		details.save()
		return HttpResponseRedirect(reverse('edit'))
	return render(request,"edit.html",content)



