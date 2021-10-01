from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None) #POST ise bilgiler alınıp form oluşur GET ise boş form oluşur
    if form.is_valid(): # clean fonksiyonu burada çağırılıyor.True/False olarak burada kontrol ediliyor.
        username = form.cleaned_data.get("username")
        password= form.cleaned_data.get("password") # clean fonksiyonunda parola doğrulaması hata vermezse sözlük yapısı şeklinde değerleri döndürüyorduk.Burada o değerleri alıyoruz.

        newUser = User(username=username) #User modelinden obje oluşturup veritabanına kaydettik.
        newUser.set_password(password) # password şifrelendi
        newUser.save()
        login(request,newUser) # kaydolduktan sonra sisteme otomatik olarak giriş yapmış oldu

        messages.info(request,"Başarıyla kayıt oldunuz.")

        return redirect("index")
    context = {
            "form" :form
        }
    return render(request,"register.html",context)
    



def loginUser(request):
    form = LoginForm(request.POST or None) 

    context = {
        "form":form
    }
    
    if form.is_valid(): # Form classındaki clean metodu otomatik olarak çalışır
        username= form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        if  user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla giriş yaptınız.")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)




def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    return redirect("index")
