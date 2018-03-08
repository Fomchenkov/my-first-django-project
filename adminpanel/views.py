from django.shortcuts import render

from adminpanel.models import Customer

from .forms import CustomerRegisterForm
from .forms import CustomerLoginForm


def index_view(request):
	if 'auth' in request.session:
		name = request.session['name']
		return render(request, 'adminpanel/panel.html', {'name': name})
	return render(request, 'adminpanel/index.html')


def logout_view(request):
	for key in list(request.session.keys()):
		del request.session[key]
	return render(request, 'adminpanel/index.html')


def register_view(request):
	if request.method == 'POST':
		form = CustomerRegisterForm(request.POST)
		if form.is_valid():
			customer = form.save(commit=False)
			customer.save()
		return render(request, 'adminpanel/index.html')
	else:
		form = CustomerRegisterForm()
		return render(request, 'adminpanel/register.html', {'form': form})


def login_view(request):
	if request.method == 'POST':
		form = CustomerLoginForm(request.POST)
		if form.is_valid():
			if Customer.objects.filter(login=request.POST['login'], password=request.POST['password']).exists():
				request.session['auth'] = True
				request.session['name'] = request.POST['login']
			else:
				return render(request, 'adminpanel/login.html', {
					'form': form,
					'message': 'Login Does Not exists',
					})
		return render(request, 'adminpanel/index.html')
	else:
		form = CustomerLoginForm()
		return render(request, 'adminpanel/login.html', {'form': form})
