from django.shortcuts import render,redirect

from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User

# Giriş yapabilmek için kullandıyoruz.
from django.contrib.auth import login

# Kullanıcının olup olmadığını kontrol ediyoruz.
from django.contrib.auth import authenticate

# Kullanıcının çıkış yapabilmesi için
from django.contrib.auth import logout

# Django mesajlarını gösterebilmek için kullanıyoruz.
from django.contrib import messages

# Create your views here.

def register(request):
    # Bize dönen bir POST var mı yok mu?
    form = RegisterForm(request.POST or None)

    # Dönen bir POST varsa ve bilgiler doğru ise
    # is_valid methodu ile forms.py dosyasındaki clean fonksiyonunu çalıştırdık.
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # Yukarıdaki değerlerle yeni kullanıcı tanımladık.
        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()

        # login sayesinde kayıt olduktan sonra sisteme giriş yapmasını sağladık.
        login(request,newUser)

        # Kayıt ve login olduktan sonra sayfaya bir mesaj gönderelim.
        messages.success(request,"Başarıyla Kayıt oldunuz..")

        # urls dosyasında adını verdiğimiz sayfaya gidecek.
        return redirect("index")

    # Eğer POST yok ise RegisterForm None dönecek ve sayfa yeniden render olacak.
    else:
        context = {
            "form" : form
        }
        return render(request,"register.html", context)

def loginUser(request):

    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }

    # Eğer bilgiler doğru ise (clean fonksiyonu çalışacak)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # Eğer bu kullanıcı varsa onu dönecek yoksa None dönecek.
        user = authenticate(username = username,
                            password = password)

        # Kullanıcı None ise tekrar login sayfası render olacak.
        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı.")
            return render(request, "login.html", context)

        # Kullanıcı döndüyse giriş yapalım.
        messages.success(request, "Başarıyla giriş yapıldı.")
        login(request, user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış yapıldı.")
    return redirect("index")

def profile(request):
    return render(request,"profile.html")