from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
# from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
# from django.core import mail
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.is_active=False
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if len(email)<16:
                messages.info(request,f'Your email {email} , couldn''t be verified  !!!')
                return redirect('register')
        
            # if not validate_email(email):
            #     messages.info(request,f'Your email {email} , couldn''t be verified  !!!')
            #     return redirect('register')
    
            # if validate_email(email) is None:
            #     messages.info(request,f'Your email {email} , couldn''t be verified  !!!')
            #     return redirect('register')

            # is_valid = validate_email(email)
            # if is_valid is None:
            #     messages.info(request,f'Your email {email} , couldn''t be verified  !!!')
            #     return redirect('register')

            form.save()
            email_subject=("This is a Confirmation email from ecopy4u")
            email_body=("Hello " + username + " , Your account has been created at ecopy4u!!!")
            Mail = EmailMessage(
                email_subject,
                email_body,
                'noreply@semy.com',
                [email]
            )
            Mail.send()
            
            #username=form.cleaned_data.get('username')
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