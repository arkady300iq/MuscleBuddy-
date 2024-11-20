from django.shortcuts import redirect, render
from authentication import forms
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        custom_user_form = forms.CustomUserForm(request.POST, request.FILES)

        if custom_user_form.is_valid():
            custom_user = custom_user_form.save()
            custom_user.save()

            login(request, custom_user)
            return redirect('main_page')  
        
    else:
        custom_user_form = forms.CustomUserForm() 

    return render(request, 'registration/register.html', {'custom_user_form': custom_user_form})

def logout_view(request):
    logout(request)
    return redirect('login')  