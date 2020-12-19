from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

            form.save()
            email_subject=("Welcome to E-copy4u")
            email_body=("Hello " + username + " , Your account has been created at ecopy4u!!!.\nHere is the link of the website:\n https://ecopy4u.herokuapp.com/")
            Mail = EmailMessage(
                email_subject,
                email_body,
                'noreply@semy.com',
                [email]
            )
            Mail.send()
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


from boards.models import boards
from colleges.models import colleges

@login_required
def mail_users(request):
    if request.user.is_superuser:
        users = User.objects.all()
        total=boards.objects.count()+colleges.objects.count()
        for user in users:
            email=user.email
            username=user.username
            email_subject=(f'Greetings From E-copy4u')
            string="\nHere is the link of the website:\n https://ecopy4u.herokuapp.com/"
            name=(f'Hello , {username} \n')
            email_body=(name + f"We have a total of {total} Papers. With your contribution, we can make much more papers available to students. Have a Nice Day" + string)
            Mail = EmailMessage(
                email_subject,
                email_body,
                'noreply@semy.com',
                [email]
            )
            Mail.send()
    return render(request,'home/home.html')




# email_subject=f'username , "Activate Your Account!!!"'
# email_body="This is a Confirmation email from ecopy4u"
# email = EmailMessage(
#     'Hello',
#     email_subject,
#     email_body,
#     [email]
# )