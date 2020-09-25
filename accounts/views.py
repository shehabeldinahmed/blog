from django.shortcuts import render ,redirect
from . form import SignupForm ,UserUpdateForm ,ProfileUpdateForm
from .models import Profile
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        
        form = SignupForm(request.POST)
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect('login')
        '''
       form = SignupForm(request.POST)    
       if form.is_valid():
           form.save()
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password1')
           user = authenticate(username=username, password=password)
           login(request,user)
           return redirect('blog-home')'''

    else:
        form =SignupForm()

    return render (request,'registration/register.html',{'form':form})  
 
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST ,instance=request.user)
        p_form = ProfileUpdateForm( request.POST,
                                    request.FILES,
                                    instance=request.user.profile
                                    )
        if u_form.is_valid() and  p_form.is_valid(): 
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateForm(instance=request.user.profile)    



    context ={'u_form':u_form ,'p_form':p_form }
    return render (request,'registration/profile.html',context)  


