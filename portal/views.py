from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse, NoReverseMatch
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required	
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User
from django.db import models
from .forms import CreateUserForm, CreateAdminForm, CreateEmployerForm, AddJobForm
from .models import Job, Profile
from .filters import JobFilter
from .decorators import permission_required1
from django.utils.module_loading import import_string
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

def registerpage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='seeker')
			user.groups.add(group)
			messages.success(request, 'Account was created for' + username + ", " + str(group))
			return redirect('/')

	context = {'form':form}
	return render(request, 'portal/register.html', context)


def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user=authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or password is incorrect')
	return render(request, 'portal/login.html')


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
# @permission_required1('groups.admin',login_url='login',raise_exception=True)
# @user_passes_test(lambda u: Group.objects.get(name='admin') in u.groups.all(),login_url='login')
def home(request):
	jobs = Job.objects.all()
	profile = Profile.objects.all()
	myfilter = JobFilter(request.GET, queryset=jobs)
	jobs = myfilter.qs
	context = {'jobs':jobs, 'profile':profile, 'myfilter':myfilter}
	return render(request, 'portal/landing.html', context)


@login_required(login_url='login')
def adminpanel(request):
	profiles = Profile.objects.all()
	context = {'profiles': profiles}
	return render(request, 'portal/adminpanel.html', context)


def joblist(request, pk_test ):
    job = Job.objects.get(id=pk_test)
    context = {'job': job}
    return render(request, 'portal/joblist.html', context)


def applyjob(request, pk):
	job = get_object_or_404(Job, id=request.POST.get('job_id'))
	job.apply.add(request.user)
	return HttpResponseRedirect(reverse('joblist', args=[str(pk)]))


def jobdetails(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'portal/jobdetails.html', context)


def addjobs(request):
	jobs = Job.objects.all()
	form = AddJobForm()
	if request.method == 'POST':
		form = AddJobForm(request.POST)
		if form.is_valid():
			form.save()	
	context = {'jobs': jobs, 'form':form}
	return render(request, 'portal/addjobs.html', context)

def appliedjobs(request):
	return render(request, 'portal/appliedjobs.html')

def candidatesearch(request):
	return render(request, 'portal/candidatesearch.html')

def profilelist(request):
	profiles = Profile.objects.all()
	context = {'profiles': profiles}
	return render(request, 'portal/profilelist.html', context)


def get_backends(request, return_tuples=False):
	backends = []
	backend_path = settings.AUTHENTICATION_BACKENDS
	for backend_path in settings.AUTHENTICATION_BACKENDS:
		backend = import_string(backend_path)()
		backends.append((backend, backend_path) if return_tuples else backend)
	
	# for backe in backends:
		# if hasattr(backe, 'has_perm'):
	context = {'backends': backends}
	return render(request, 'portal/backend.html', context)
    # if not backends:
    #     raise ImproperlyConfigured(
    #         'No authentication backends have been defined. Does '
    #         'AUTHENTICATION_BACKENDS contain anything?'
    #     )
    #return backends

def adminregisterpage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='admin')
			user.groups.add(group)
			messages.success(request, 'Account was created for' + username + ", " + str(group))
			return redirect('/')

	context = {'form':form}
	return render(request, 'portal/adminregister.html', context)


def employerregisterpage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='employer')
			user.groups.add(group)
			messages.success(request, 'Account was created for' + username + ", " + str(group))
			return redirect('/')

	context = {'form':form}
	return render(request, 'portal/employerregister.html', context)