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


def viewreport(request):
	o = onetoone.objects.raw(f'select onetooneid from onemoreapp_onetoone where user_id = {request.user.id}')[len(onetoone.objects.raw(f'select onetooneid from onemoreapp_onetoone where user_id = {request.user.id}'))-1]
	w = weeklypresentation.objects.raw(f'select weeklypresentationid from onemoreapp_weeklypresentation where user_id = {request.user.id}')[len(weeklypresentation.objects.raw(f'select weeklypresentationid from onemoreapp_weeklypresentation where user_id = {request.user.id}'))-1]
	d = dailypresentation.objects.raw(f'select dailypresentationid from onemoreapp_dailypresentation where user_id = {request.user.id}')[len(dailypresentation.objects.raw(f'select dailypresentationid from onemoreapp_dailypresentation where user_id = {request.user.id}'))-1]
	s = socials.objects.raw(f'select socialsid from onemoreapp_socials where user_id = {request.user.id}')[len(socials.objects.raw(f'select socialsid from onemoreapp_socials where user_id = {request.user.id}'))-1]
	v = visitors.objects.raw(f'select visitorsid from onemoreapp_visitors where user_id = {request.user.id}')[len(visitors.objects.raw(f'select visitorsid from onemoreapp_visitors where user_id = {request.user.id}'))-1]
	rg = referralsgiven.objects.raw(f'select referralsgivenid from onemoreapp_referralsgiven where user_id = {request.user.id}')[len(referralsgiven.objects.raw(f'select referralsgivenid from onemoreapp_referralsgiven where user_id = {request.user.id}'))-1]
	rt = referralstaken.objects.raw(f'select referralstakenid from onemoreapp_referralstaken where user_id = {request.user.id}')[len(referralstaken.objects.raw(f'select referralstakenid from onemoreapp_referralstaken where user_id = {request.user.id}'))-1]
	content = {
		'onetopic' : o.onetopic,
		'onetime' : o.oneduration,
		'onedate' : o.onedate,
		'weeklytopic' : w.weektopic,
		'weeklytime' : w.weekduration,
		'weeklydate' :w.weekdate,
		'dailytopic' : d.dailytopic,
		'dailytime' : d.dailyduration,
		'dailydate' : d.dailydate,
		'soctopic' : s.socialstopic,
		'soctime' : s.socialsduration,
		'socdate' : s.socialsdate,
		'vistopic' : v.visitorstopic,
		'vistime' : v.visitorsduration,
		'visdate' : v.visitorsdate,
		'refgtopic' : rg.giventopic,
		'refgtime' : rg.givenduration,
		'refgdate' : rg.givendate,
		'refttopic' : rt.takentopic,
		'refttime' : rt.takenduration,
		'reftdate' : rt.takendate
	}
	return render(request,"view-report.html",content)



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
		social_s.socialsplace = request.POST['place']
		social_s.socialstopic = request.POST['Topicname']
		social_s.socialsduration = request.POST['Time']
		social_s.socialsdate = request.POST['Date']
		social_s.save()
		return HttpResponseRedirect('jvtconnect')


def visitor(request):
	if request.method == "POST":
		visitor_s = visitors()
		visitor_s.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		visitor_s.visitorscount = request.POST['howmany']
		visitor_s.visitorstopic = request.POST['Topicname']
		visitor_s.visitorsduration = request.POST['Time']
		visitor_s.visitorsdate = request.POST['Date']
		visitor_s.save()
		return HttpResponseRedirect('jvtconnect')


def given(request):
	if request.method == "POST":
		give = referralsgiven()
		give.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		give.givencount = request.POST['howmany']
		give.giventopic = request.POST['Topicname']
		give.givenduration = request.POST['Time']
		give.givendate = request.POST['Date']
		give.save()
		return HttpResponseRedirect('jvtconnect')


def taken(request):
	if request.method == "POST":
		take = referralstaken()
		take.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		take.takencount = request.POST['howmany']
		take.takentopic = request.POST['Topicname']
		take.takenduration = request.POST['Time']
		take.takendate = request.POST['Date']
		take.save()
		return HttpResponseRedirect('jvtconnect')






