from django import http
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
import json
from .models import orders, user_query,hostel,tiffinservice,laundry,library
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.


amount_sum=100
mode=1
my_id=1
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
k=hostel.objects.all()
states=set("")
cities=set("")
for i in k:
    states.add(i.hostel_state)
    cities.add(i.hostel_city)
def rentalserviceprovider(request):
    if request.method=="POST" and request.FILES['image1'] and request.FILES['image2']:
        name=request.POST['name']
        state=request.POST['inputState']
        city=request.POST['inputCity']
        area=request.POST['area']
        pincode=request.POST['inputZip']
        address=request.POST['Address']
        rent=request.POST['rent']
        deposit=request.POST['deposit']
        contactnumber=request.POST['contact']
        description=request.POST['description']
        mess=request.POST.get('mess',"off")
        if mess=="on":
            mess=1
        else:
            mess=0
        mealtype=request.POST.get('veg',"off")
        if mealtype=="on":
            mealtype="non-veg"
        else:
            mealtype="veg"
        ac=request.POST.get('ac',"off")
        if ac=="on":
            ac=1    
        else:
            ac=0
        visitor=request.POST.get('visitor',"off")
        if visitor=="on":
            visitor=1 
        else:
            visitor=0   
        water=request.POST.get('water',"off")
        if water=="on":
            water=1
        else:
            water=0
        room=request.POST.get('room',"off")
        if room=="on":
            room=1
        else:
            room=0 
        image1 = request.FILES['image1']
        fs = FileSystemStorage()
        filename = fs.save(image1.name, image1)
        url1 = fs.url(filename)
        print(url1)
        image2 = request.FILES['image2']
        fs = FileSystemStorage()
        filename = fs.save(image2.name, image2)
        url2 = fs.url(filename)
        print(2)
        url1=url1[7:]
        url2=url2[6:]
        ins=hostel(hostel_images1=url1,hostel_image2=url2,hostel_name=name,hostel_state=state,hostel_city=city,hostel_area=area,hostel_pincode=pincode, hostel_address=address,hostel_rent=rent,hostel_deposit=deposit,hostel_contactnumber=contactnumber,hostel_description=description,hostel_mess=mess,hostel_mealtype=mealtype,hostel_ac=ac,hostel_vistorentry=visitor,hostel_watercooler=water,hostel_roomcleaning=room)               
        ins.save()  
        messages.info(request,"Your details are submitted, Thank you for choosing us!")      
    return render(request,"display/rentalserviceprovider.html",{'states':states,'cities':cities})


def tiffinserviceprovider(request):
    if request.method=="POST" and request.FILES['image1'] and request.FILES['image2']:
        tiffinservice_name=request.POST['name']
        tiffinservice_state=request.POST['inputState']
        tiffinservice_city=request.POST['inputCity']
        tiffinservice_area=request.POST['area']
        tiffinservice_address=request.POST['Address']
        tiffinservice_pincode=request.POST['pincode']
        tiffinservice_price=request.POST['price']
        tiffinservice_contactnumber=request.POST['contact']
        tiffinservice_mealtype=request.POST['mealtype']
        if tiffinservice_mealtype == "YES" or tiffinservice_mealtype == "yes":
            tiffinservice_mealtype="non-veg"
        else:
            tiffinservice_mealtype="veg"
        tiffinservice_mealsperday=request.POST['mealperday']
        tiffinservice_description=request.POST['description']
        image1 = request.FILES['image1']
        fs = FileSystemStorage()
        filename = fs.save(image1.name, image1)
        url1 = fs.url(filename)
        print(url1)
        image2 = request.FILES['image2']
        fs = FileSystemStorage()
        filename = fs.save(image2.name, image2)
        url2 = fs.url(filename)
        print(2)
        url1=url1[7:]
        url2=url2[6:]
        ins=tiffinservice(tiffinservice_images1=url1,tiffinservice_image2=url2,tiffinservice_description=tiffinservice_description,tiffinservice_mealsperday=tiffinservice_mealsperday,tiffinservice_contactnumber=tiffinservice_contactnumber,tiffinservice_name=tiffinservice_name,tiffinservice_state=tiffinservice_state,tiffinservice_city=tiffinservice_city,tiffinservice_area=tiffinservice_area,tiffinservice_pincode=tiffinservice_pincode,tiffinservice_address=tiffinservice_address,tiffinservice_price=tiffinservice_price)
        ins.save()
        messages.info(request,"Your details are submitted, Thank you for choosing us!")
    return render(request,"display/tiffinserviceprovider.html",{'states':states,'cities':cities})


def laundryserviceprovider(request):
    if request.method=="POST" and request.FILES['image1'] :
        name=request.POST['name']
        state=request.POST['inputState']
        city=request.POST['inputCity']
        area=request.POST['area']
        pincode=request.POST['inputZip']
        address=request.POST['Address']
        deposit=request.POST['deposit']
        contactnumber=request.POST['contact']
        description=request.POST['description']
        image1 = request.FILES['image1']
        fs = FileSystemStorage()
        filename = fs.save(image1.name, image1)
        url1 = fs.url(filename)
        print(url1)
        url1=url1[7:]
        ins=laundry(laundry_images1=url1,laundry_name=name,laundry_state=state,laundry_city=city,laundry_area=area,laundry_pincode=pincode, laundry_address=address,laundry_price=deposit,laundry_contactnumber=contactnumber,laundry_description=description)               
        ins.save()  
        messages.info(request,"Your details are submitted, Thank you for choosing us!") 
    return render(request,"display/laundryserviceprovider.html",{'states':states,'cities':cities})


def libraryserviceprovider(request):
     if request.method=="POST" and request.FILES['image1'] :
        name=request.POST['name']
        state=request.POST['inputState']
        city=request.POST['inputCity']
        area=request.POST['area']
        pincode=request.POST['inputZip']
        address=request.POST['Address']
        deposit=request.POST['deposit']
        contactnumber=request.POST['contact']
        description=request.POST['description']
        image1 = request.FILES['image1']
        fs = FileSystemStorage()
        filename = fs.save(image1.name, image1)
        url1 = fs.url(filename)
        print(url1)
        url1=url1[7:]
        ins=library(library_images1=url1,library_name=name,library_state=state,library_city=city,library_area=area,library_pincode=pincode, library_address=address,library_deposit=deposit,library_contactnumber=contactnumber,library_description=description)               
        ins.save()  
        messages.info(request,"Your details are submitted, Thank you for choosing us!") 
     return render(request,"display/libraryserviceprovider.html",{'states':states,'cities':cities})


def allservices(request):
    return render(request,"display/allservices.html")

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
                        user.save()
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

person=""
def login(request):
    global person
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
            person=username
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
    global mode
    mode = 1
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
    global mode
    mode = 2
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
    global mode
    mode = 3
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
    global mode
    mode = 4
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
    hostel_detail = hostel.objects.get(pk=hostel_id)
    global my_id
    my_id=hostel_id
    global amount_sum
    if hostel_detail:
        demo = {
                    'hostel' : hostel_detail,
                }
        
        return render(request,"display/description_page.html",demo)
    else:
	    response = "Hostel with id=" + str(id) + " not found."
	    return HttpResponse(response)

def tiffin_description_page(request, tiffinservice_id):
    global my_id
    my_id=tiffinservice_id
    hostel_detail = tiffinservice.objects.get(pk=tiffinservice_id)
    if hostel_detail:
        demo = {
                    'hostel' : hostel_detail,
                }
        return render(request,"display/tiffin_desc.html",demo)
    else:
	    response = "Tiffin Service with id=" + str(id) + " not found."
	    return HttpResponse(response)

def library_description_page(request, library_id):
    global my_id
    my_id=library_id
    hostel_detail = library.objects.get(pk=library_id)
    if hostel_detail:
        demo = {
                    'hostel' : hostel_detail,
                }
        return render(request,"display/lib_desc.html",demo)
    else:
	    response = "Library with id=" + str(id) + " not found."
	    return HttpResponse(response)

def laundry_description_page(request, laundry_id):
    global my_id
    my_id=laundry_id
    hostel_detail = laundry.objects.get(pk=laundry_id)
    if hostel_detail:
        demo = {
                    'hostel' : hostel_detail,
                }
        return render(request,"display/laundry_desc.html",demo)
    else:
	    response = "Laundry with id=" + str(id) + " not found."
	    return HttpResponse(response)


def check_out(request):
    global amount_sum
    amount_sum=0
    global mode
    if mode == 1:
        amount_sum=hostel.objects.get(pk=my_id).hostel_rent
        amount_sum+=hostel.objects.get(pk=my_id).hostel_deposit
        demo={
        'amount':amount_sum,
        'my_id':my_id,
        'mode':mode
        }
        amount_sum=0
    elif mode == 2:
        amount_sum=tiffinservice.objects.get(pk=my_id).tiffinservice_price
        demo={
        'amount':amount_sum,
        'my_id':my_id,
        'mode':mode
          }
        amount_sum=0  
    elif mode == 3:
        amount_sum=laundry.objects.get(pk=my_id).laundry_price
        demo={
        'amount':amount_sum,
        'my_id':my_id,
        'mode':mode
        }
        amount_sum=0
    elif mode == 4:
        amount_sum=library.objects.get(pk=my_id).library_deposit
        demo={
        'amount':amount_sum,
        'my_id':my_id,
        'mode':mode
         }
        amount_sum=0
    return render(request,"display/checkout.html",demo)
amount_sum=0
def paymentsuccess(request):
    body=json.loads(request.body)
    #print('body:',body)
    global person
    if (body['mode']) == '1':
        name=hostel.objects.get(pk=body['productId']).hostel_name
        orders.objects.create(customer_username=person,amount_paid=body['amount'],item_type="rental",product_id=body['productId'],product_name=name,transaction_success=True)    
        print(name,body['amount'],"rental",body['productId'])
    elif (body['mode']) == '2':
        name=tiffinservice.objects.get(pk=body['productId']).tiffinservice_name
        orders.objects.create(customer_username=person,amount_paid=body['amount'],item_type="tiffinservice",product_id=body['productId'],product_name=name,transaction_success=True)    
        print(name,body['amount'],"tiffin",body['productId'])
    elif (body['mode']) == '3':
        name=laundry.objects.get(pk=body['productId']).laundry_name
        print(name,body['amount'],"laundry",body['productId'])
        orders.objects.create(customer_username=person,amount_paid=body['amount'],item_type="laundry",product_id=body['productId'],product_name=name,transaction_success=True)    
    elif (body['mode']) == '4':
        name=library.objects.get(pk=body['productId']).library_name
        print(name,body['amount'],"library",body['productId'])
        orders.objects.create(customer_username=person,amount_paid=body['amount'],item_type="library",product_id=body['productId'],product_name=name,transaction_success=True)    
    person=""
    success()
    return JsonResponse("Yay! ,Payment Completed!",safe=False)

def success(request):
    return render(request,"display/success.html")