from django import http
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import user_query,hostel,tiffinservice,laundry,library
# Create your views here.




def home_page(request):
    if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            """value_con = {
            'name' :name,
            'email' :email ,
            'phone' :phone,
            }"""
            error_query =""
            if not name:
                error_query = "Enter your name"
            if not email:
                error_query = "Enter your email"
            if not phone:
                error_query = "Enter your contact number"
            if len(phone) < 10:
                error_query = "Enter a valid phone number"  
            if not message:
                error_query = "Enter your message!"
            if not error_query:                  
                query = user_query(user_name = name,user_email = email,user_number = phone,user_querry = message)
                query.save()
                messages.info(request,"Your message was sent, Thank you!")
                return redirect('/')
            else:
                datac ={
                'error_con' : error_query,
                #'values_con' : value_con
            }   
            return render(request,"display/index.html",datac)  

    return render(request,"display/index.html")


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # validation
        value = {
            'name' :name,
            'username' :username,
            'email' :email ,
        }
        agree = request.POST.get('agree-term','off')
        error_message = ""
        if not name:
            error_message = "Name required!!"
        elif len(name) < 3:
            error_message = "Name should be atleast of 3 characters!!"
        elif not username:
            error_message = "Username can't be blank!!"
        elif len(username) < 3:
            error_message = "Username should be atleast of 3 characters!!" 
        elif not email:
            error_message = "Email Required !!" 
        elif email[0]=='@':
            error_message = "invalid email address !!"
        elif not pass1:
            error_message = "Password Required !!"
        elif len(pass1) < 6:
            error_message = "Password can't be smaller than 6 characters!!"
        elif not pass2:
            error_message = "Confirm Password can't be blank!!"      
        

        if not error_message:
            if pass1==pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already in use!')
                    return redirect('/register/')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Your email id already exists!')
                    return redirect('/register/')
                else:        
                    if agree == "on":
                        user = User.objects.create_user(first_name=name,username=username, email=email,password = pass1)
                        user.save();
                        return redirect('/login/')
                    else:
                        messages.info(request,"Process can't be completed without agreeing to TERMS and CONDITIONS")
                        return redirect('/register/') 
                
            else:
                messages.info(request,"Password doesn't match") 
                return redirect('/register/')    
        else:
            data ={
                'error' : error_message,
                'values' : value
            }   
            return render(request,"display/register.html",data)      
           

    else:
        return render(request,"display/register.html") 


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not username:
            messages.info(request,"To log in, enter your username!")
            return redirect("/login/")
        elif not password:
            messages.info(request,"To log in, enter your password!")
            return redirect("/login/")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('/login/')    
    else:    
        return render(request,"display/login.html") 

def logout(request):
    auth.logout(request)
    return redirect('/')  

def about(request):
    return render(request,"display/aboutus.html") 


def message(request):
    return render(request,"display/message.html")              

def rental(request):
    if request.method == "GET":
        pincode = request.GET.get('pincode',"")
        city=request.GET.get('city',"")
        ac = request.GET.get('ac',"off")
        visitor_entry = request.GET.get('visitor_entry',"off")
        water_cooler = request.GET.get('water_cooler',"off")
        room_cleaning = request.GET.get('room_cleaning',"off")
        all_hostel_name = hostel.objects.all()
        if pincode:
            all_hostel_name = all_hostel_name.filter(hostel_pincode = pincode)
            if not all_hostel_name :
                return render(request,"display/pincode_not_found.html") 
        if visitor_entry == "on":
            all_hostel_name = all_hostel_name.filter(hostel_vistorentry=1)
        if ac == "on":
            all_hostel_name = all_hostel_name.filter(hostel_ac=1)
        if water_cooler == "on":
            all_hostel_name = all_hostel_name.filter(hostel_watercooler=1)
        if room_cleaning == "on":
            all_hostel_name = all_hostel_name.filter(hostel_roomcleaning=1)
        if visitor_entry=="off" and ac=="off" and water_cooler=="off" and room_cleaning=="off" and pincode=="":
            all_hostel_name = hostel.objects.all()
        if city!='':
            all_hostel_name = all_hostel_name.filter(hostel_city__exact = city)
        if not all_hostel_name:
            return render(request,"display/pincode_not_found.html")
        demo = {
                    'hostel_list' : all_hostel_name,
                    'pincode': pincode,
                    'city': city
                }
        return render(request,"display/rental.html",demo)
    else:
        all_hostel_name = hostel.objects.all()
        demo2 = {
                'hostel_list' : all_hostel_name,
        }
    return render(request,"display/rental.html",demo2)


def tiffin(request):
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        if pincode:
            all_tiffin_name = tiffinservice.objects.filter(tiffinservice_pincode = pincode)
            if all_tiffin_name:
                demo = {
                    'tiffin_list' : all_tiffin_name,
                }
                return render(request,"display/tiffin.html",demo)
            return render(request,"display/pincode_not_found.html")
        all_tiffin_name = tiffinservice.objects.all()
        demo = {
                    'tiffin_list' : all_tiffin_name,
                }
        return render(request,"display/tiffin.html",demo)

    else:
        all_tiffin_name = tiffinservice.objects.all()
        demo2 = {
                'tiffin_list' : all_tiffin_name,
        }
    return render(request,"display/tiffin.html",demo2)
    

def misc(request):
    return render(request, "display/misc.html")

def laundary(request):
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        if pincode:
            all_laundry_name = laundry.objects.filter(laundry_pincode = pincode)
            if all_laundry_name:
                demo = {
                    'laundry_list' : all_laundry_name,
                }
                return render(request,"display/laundry.html",demo)
            return render(request,"display/pincode_not_found.html")
        all_laundry_name = laundry.objects.all()
        demo = {
                    'laundry_list' : all_laundry_name,
                }
        return render(request,"display/laundry.html",demo)

    else:
        all_laundry_name = laundry.objects.all()
        demo2 = {
                'laundry_list' : all_laundry_name,
        }
    return render(request,"display/laundry.html",demo2)

def lib(request):
    if request.method == "GET":
        pincode = request.GET.get('search',"")
        if pincode:
            all_lib_name = library.objects.filter(library_pincode = pincode)
            if all_lib_name:
                demo = {
                    'library_list' : all_lib_name,
                }
                return render(request,"display/library.html",demo)
            return render(request,"display/pincode_not_found.html")
        all_lib_name = library.objects.all()
        demo = {
                    'library_list' : all_lib_name,
                }
        return render(request,"display/library.html",demo)

    else:
        all_lib_name = library.objects.all()
        demo2 = {
                'library_list' : all_lib_name,
        }
    return render(request,"display/library.html",demo2)


def hostel_description_page(request, hostel_id):

    hostel_detail = hostel.objects.filter(pk=hostel_id)
    if hostel_detail:
        demo = {
                    'hostel_list' : hostel_detail,
                }
        return render(request,"display/description_page.html",demo)
    else:
	    response = "Hostel with id=" + str(id) + " not found."
	    return HttpResponse(response)

def tiffin_description_page(request, tiffinservice_id):

    hostel_detail = tiffinservice.objects.filter(pk=tiffinservice_id)
    if hostel_detail:
        demo = {
                    'hostel_list' : hostel_detail,
                }
        return render(request,"display/tiffin_desc.html",demo)
    else:
	    response = "Tiffin Service with id=" + str(id) + " not found."
	    return HttpResponse(response)

def library_description_page(request, library_id):

    hostel_detail = library.objects.filter(pk=library_id)
    if hostel_detail:
        demo = {
                    'hostel_list' : hostel_detail,
                }
        return render(request,"display/lib_desc.html",demo)
    else:
	    response = "Library with id=" + str(id) + " not found."
	    return HttpResponse(response)

def laundry_description_page(request, laundry_id):

    hostel_detail = laundry.objects.filter(pk=laundry_id)
    if hostel_detail:
        demo = {
                    'hostel_list' : hostel_detail,
                }
        return render(request,"display/laundry_desc.html",demo)
    else:
	    response = "Laundry with id=" + str(id) + " not found."
	    return HttpResponse(response)
def success(request):
    return render(request,"display/success.html")

def check_out(request):
    return render(request,"display/checkout.html")
