from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import userdetails
from django.views.decorators.cache import never_cache

    # Create your views here---------------
@never_cache
def homepage(request):
    print('hiifirst')
    if 'username' in request.session :
    #if request.user.is_authenticated:
        return redirect('welcome')
    else:
        # print(request)
        # print(rsequest.method)
        if request.method == 'POST':
            username=request.POST['username']
            password=request.POST['password']
            print('hiiyy post inside')
            #user =authenticate(username=username,password=password)
            user=userdetails.objects.filter(username=username,password=password).count()
            print('hiiyy')
            if user==1:
            #if user is not None :
                request.session['username'] = username
                print(request.session)
                print('hii')
                #login(request,user)
                #if 'username' in request.session :
                #if request.user.is_authenticated:
                return redirect('welcome')  
            else :
                return HttpResponse('Invalid username or password')
            #print('hii homehtml')
        else :
            return render(request,'home.html')
            



@never_cache  #home page of user-----------------------
def welcome(request):
    if 'username' in request.session :
        return render(request,'welcome.html')
    else:
        return render(request,'home.html')


  #LOGOUT ---------------------------------
def logout_user(request):
    if 'username' in request.session :
        del request.session['username']
        return redirect('homepage')



    #Signup page of user---------------------
def signuppage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Re enter your password")
        else :
            my_user=userdetails.objects.create(username=uname,email=email,password=pass1)
            my_user.save()
            return redirect('homepage')
    return render(request,'signup.html')  



@never_cache    #admin lologin page----------------------
def admin_login(request) :
    if 'username' in request.session :
        return redirect('admin_userlist')
    else :
        if request.method=='POST':
            admin_name=request.POST.get('admin_name')
            admin_password=request.POST.get('admin_password')
            user=authenticate(request,username=admin_name,password=admin_password)
            #if admin_password != 'siju11':
            if user is not None :
                request.session['username'] = admin_name
                return redirect('admin_userlist')
            else:
                return HttpResponse('invalid password or username')                         
        else :
            return render(request,'adminlogin.html')




def logout_admin(request):
    if 'username' in request.session :
        #print('admin seession delected')
        del request.session['username']
        return redirect('homepage')


    #admin home page
@never_cache
def admin_userlist(request):
    #if 'admin_name' in request.session :
        userlist = userdetails.objects.all().order_by('id')
        #customers = Customer.objects.all().order_by('id')
        return render(request,'admin_userlist.html',{'tablelist': userlist})
        #return redirect('admin_userlist')
    #else :
        #return render(request,'adminlogin.html')



    #add user
def add_user(request):
    if request.method == "POST":
        addname= request.POST.get('addname')
        addemail=request.POST.get('addemail')
        addpassword=request.POST.get('addpassword')
        emp = userdetails(
            username = addname,
            email = addemail,
            password =addpassword
        )   
        emp.save()
        return redirect('admin_userlist')  
    return render(request,'add_user.html')



    #udating user values showing
def value_update(request):
   
    values=userdetails.object.get(id=request.user.id)
    return render(request,"update_user.html",{'values':values})



    #update user-----------------------------
def update_user(request):
    if request.method == 'POST':
        id=request.GET['uid']
        updateusername=request.POST['updateusername']
        updateemail=request.POST['updateemail']
        updatepassword=request.POST['updatepassword']

        userdetails.objects.filter(id=id).update(

            username=updateusername,
            email=updateemail,
            password=updatepassword,
        )
        #userupdate.save()
        return redirect('admin_userlist')
    else:  
        id=request.GET['uid']
        member=userdetails.objects.filter(id=id)
        for i in member:
            print(i.username)
        return render(request,'update_user.html',{'updateuser':member})


    
    #delte userz-----------------------------
def delect_user(request):
    id=request.GET.get('id')
    print('request.GET')
    delete_user=userdetails.objects.filter(id=id).all()
    delete_user.delete()
    return redirect('admin_userlist')
    #return render(request,'delete_user.html')



