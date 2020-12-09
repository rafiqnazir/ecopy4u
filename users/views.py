from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            # email=form.cleaned_data.get('email')
            # email_subject=f'username , "Activate Your Account!!!"'
            # email_body="This is a Confirmation email from ecopy4u"
            # email = EmailMessage(
            #     'Hello',
            #     email_subject,
            #     email_body,
            #     [email]
            # )
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!!!')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    content={
        'title':'User Registration',
        'form':form
    }
    return render(request,'users/register.html',content)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated!!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' :  u_form,
        'p_form' : p_form,
    }
    return render(request,'users/profile.html',context)




# email_subject=f'username , "Activate Your Account!!!"'
# email_body="This is a Confirmation email from ecopy4u"
# email = EmailMessage(
#     'Hello',
#     email_subject,
#     email_body,
#     [email]
# )