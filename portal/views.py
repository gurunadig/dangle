from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import Job, Profile
from .filters import JobFilter

def registerpage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for' + user)
			return redirect('login')

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
def home(request):
	jobs = Job.objects.all()
	profile = Profile.objects.all()

	myfilter = JobFilter(request.GET, queryset=jobs)
	jobs = myfilter.qs
	context = {'jobs':jobs, 'profile':profile, 'myfilter':myfilter}
	return render(request, 'portal/landing.html', context)


def profile(request):
    profile = Profile.objects.all()
    context = {'profile': profile}
    return render(request, 'portal/profile.html', context)


def joblist(request, pk_test ):
    job = Job.objects.get(id=pk_test)
    context = {'job': job}
    return render(request, 'portal/joblist.html', context)

def applyjob(request, pk):
	job = get_object_or_404(Job, id=request.POST.get('job_id'))
	job.apply.add(request.user)
	return HttpResponseRedirect(reverse('joblist', args=[str(pk)]))
