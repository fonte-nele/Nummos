from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.forms import ModelForm
from accounts.models import Empresa

# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#log the user in
			login(request, user)
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/')
			#log in the user
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form': form}) 

def logout_page(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/')

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nameResp', 'nameEst','segmento','faturamento','cidade','email', 'telefone']  
        labels = {
            "nameResp": "Nome do responsável",
            "nameEst": "Nome do estabelecimento",
            "segmento": "Segmento",
            "faturamento": "Faturamento mensal",
            "cidade": "Cidade",
            "email": "Email",
            "telefone": "Telefone",
        }
    # Validação
    def is_valid(self):
        
        valid = super(EmpresaForm, self).is_valid()
        
        if not valid:
            return valid
        telefone = self.cleaned_data['telefone']
        try: 
            int(telefone)
            if(self.cleaned_data['faturamento'] == 0):
                self.add_error('faturamento','O faturamento deve ser diferente de zero')
                return False
            return True
        except ValueError:
            self.add_error('telefone', 'Digite apenas números para o telefone')
            return False



def voltar(request, template_name='app/index.html'):
	return render(request, template_name)

def cadastroEmpresa(request, template_name='accounts/login.html'):
    empresa = Empresa()

    empresa.telefone = "Digite telefone com ID do país e DDD"
    form = EmpresaForm(request.POST or None, instance=empresa)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, template_name, {'form':form})