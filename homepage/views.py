from django.shortcuts import render,redirect
from homepage.models import userinfo,Services
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import check_password

email_map={}

# Create your views here.
def home(request):
    if 'user_id' in request.session:
        return redirect('/dashboard/')
    return render(request, 'homepage.html')

def services(request):
    service_data = Services.objects.all()

    data = {
        'services':service_data
    }

    return render(request,'services.html',data)
def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = userinfo.objects.get(email=email)
        except:
            messages.error(request, "User not found")
            return render(request, 'login.html')

        if not user.is_verified:
            messages.error(request, "Email not verified")
            return render(request, 'login.html')

        if check_password(password, user.password):
            request.session['user_id'] = user.id  # ✅ store session
            request.session['name'] = user.name
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid password")
    return render(request, 'login.html')


    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def signup(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if userinfo.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'signup.html')

        hashed_password = make_password(password)
        user = userinfo(name=name, email=email, password=hashed_password)
        user.save()

        token = get_random_string(length=32)
        email_map[token] = user.id

        send_mail(
            subject='Verify your email',
            message=f'Click the link to verify your email: http://localhost:8000/verify/{token}/',
            from_email='pranabroy.bnmpc@gmail.com',
            recipient_list=[email],
            fail_silently=False

        )
        return render(request, 'check_email.html')
        

    return render(request, 'signup.html')


def verify_email(request, token):
    user_id = email_map.get(token)
    print(id)
    if user_id:
        user = userinfo.objects.get(id=user_id)
        user.is_verified = True
        user.save()
        del email_map[token]  # remove used token
        return render(request, 'email_verified.html')

    return render(request, 'invalid_token.html')
