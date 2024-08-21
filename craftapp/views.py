from django import forms
from django.shortcuts import redirect, render , get_object_or_404
from django.http import Http404
from.models import Reg_seller,Reg_tutor,Reg_user,craft_selling,accessories_selling,user,Cart,pay,Craftcart,Video
import razorpay
from django.conf import settings
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest 
from razorpay import Client

razorpay_client = Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))



# Create your views here.
def index(request):
    return render(request,'index.html')
def userhome(request):
    return render(request,'userhome.html')

def sellerhome(request):
    return render(request,'sellerhome.html')
def tutorhome(request):
    return render(request,'tutorhome.html')

def about(request):
    return render(request,'about.html')

# def appointment(request): 
#     if request.method=="POST":
#         n=request.POST.get("username")
#         cid=request.POST.get("Customerid")
#         cphone=request.POST.get("Customerphonenumber")
#         cplace=request.POST.get("Customerplace")

#         (name=n,customerid=cid,customerphone=cphone,customerplace=cplace).save()
#         return render(request,'appointment.html')

def call_to_action(request):
    return render(request,'call-to-action.html')

def classes(request):

    return render(request,'classes.html')

def contact(request):
    return render(request,'contact.html')

def facility(request):
    return render(request,'facility.html')

def index(request):
    return render(request,'index.html')

def team(request):
    return render(request,'team.html')

def testmonial(request):
    return render(request,'testimonial.html')



def seller_reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        number = request.POST.get('number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        # Check if the username already exists
        if Reg_seller.objects.filter(username=username).exists():
            msge = 'Username already exists. Please choose a different username.'
            return render(request, 'seller_reg.html', {'me': msge})
        elif password != c_password:
            msge = 'Password and Confirm Password do not match'
            return render(request, 'seller_reg.html', {'me': msge})
        else:
            # Save the seller registration if the username is unique and passwords match
            Reg_seller.objects.create(name=name, username=username, number=number, email=email, password=password)
            msg1 = 'Successfully registered'
            return render(request, 'sellerlogin.html', {'mi': msg1})
    else:
        return render(request, 'seller_reg.html')

 
def sellerlogin(request):
   if request.method=='POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      cr = Reg_seller.objects.filter(username=username,password=password)
      if cr:
         details = Reg_seller.objects.get(username=username,password=password)
         Email = details.email
         username= details.username
         request.session['seller']=Email
         request.session['sellername']=username

         return render(request,'sellerhome.html')
      else :
            if not Reg_seller.objects.filter(username=username).exists():
                msge='your username is incorrect'
                return render(request,'sellerlogin.html',{'me':msge})     
            else:
                msge='your password is incorrect'
                return render(request,'sellerlogin.html',{'me':msge})
   else:
         return render(request,'sellerlogin.html')

def  user_reg(request):
    if request.method =='POST':
      name = request.POST.get('name')
      username = request.POST.get('username')
      number= request.POST.get('number')
      email = request.POST.get('email')
      address = request.POST.get('address')
      password = request.POST.get('password')
      c_password = request.POST.get('c_password')

      if   password != c_password :
            msge = 'Password and Confirm Password do not match'
            return render(request, 'user_reg.html', {'me': msge})
      else:
        Reg_user(name=name,address=address,username=username,number=number,email=email,password=password).save()
        return render(request,'userlogin.html')
    else:
        return render(request,'user_reg.html')

def userlogin(request):
    if request.method=='POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      cr = Reg_user.objects.filter(username=username,password=password)
      if cr:
         details = Reg_user.objects.get(username=username,password=password)
         Email = details.email
         username= details.username
         request.session['user']=Email
         request.session['username']=username

         return render(request,'userhome.html')
      else :
            if not Reg_user.objects.filter(username=username).exists():
                msge='your username is incorrect'
                return render(request,'userlogin.html',{'me':msge})     
            else:
                msge='your password is incorrect'
                return render(request,'userlogin.html',{'me':msge})
    else:
         return render(request,'userlogin.html')
   

def tutor_reg(request):
    if request.method =='POST':
      name = request.POST.get('name')
      username = request.POST.get('username')
      number= request.POST.get('number')
      email = request.POST.get('email')
      address = request.POST.get('address')
      password = request.POST.get('password')
      c_password = request.POST.get('c_password')

      if   password != c_password :
            msge = 'Password and Confirm Password do not match'
            return render(request, 'tutor_reg.html', {'me': msge})
      else:
        Reg_tutor(name=name,address=address,username=username,number=number,email=email,password=password).save()
        msg = 'Succesfully Registered'
        return render(request,'tutorlogin.html',{'msg':msg})
    else:
        return render(request,'tutor_reg.html')
    
def tutorlogin(request):
   if request.method=='POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      cr = Reg_tutor.objects.filter(username=username,password=password)
      if cr:
         details = Reg_tutor.objects.get(username=username,password=password)
         Email = details.email
         username= details.username
         request.session['tutor']=Email
         request.session['tutorname']=username

         return render(request,'tutorhome.html')
      else :
            if not Reg_tutor.objects.filter(username=username).exists():
                msge='your username is incorrect'
                return render(request,'tutorlogin.html',{'me':msge})     
            else:
                msge='your password is incorrect'
                return render(request,'tutorlogin.html',{'me':msge})
   else:
         return render(request,'tutorlogin.html')
   
def craftselling(request):

    ownername=request.session['sellername']

    if request.method =='POST':
      print(ownername)
      item_name = request.POST.get('item_name')
      category= request.POST.get('category')
      description = request.POST.get('description')
      price = request.POST.get('price')
      quantity = request.POST.get('quantity')
      image = request.FILES['image']
      craft_material = request.POST.get('craft_material') 
      size = request.POST.get('size') 
      craft_selling(owner_name=ownername,item_name=item_name,craft_material=craft_material,category=category, description=description, price=price,image=image, quantity=quantity,size=size).save()
      return render(request,'sellerhome.html')
     
    else:
        return render(request,'craft_selling.html',{'name':ownername})
    

def accessory_selling(request):

    ownername=request.session['sellername']

    if request.method =='POST':
      print(ownername)
      item_name = request.POST.get('item_name')
      category= request.POST.get('category')
      description = request.POST.get('description')
      price = request.POST.get('price')
      quantity = request.POST.get('quantity')
      image = request.FILES['image']
      accessory_type = request.POST.get('accessory_type') 
      size = request.POST.get('size') 
      accessories_selling(owner_name=ownername,item_name=item_name,accessory_type=accessory_type,category=category, description=description, price=price,image=image, quantity=quantity,size=size).save()
      return render(request,'sellerhome.html')
     
    else:
        return render(request,'accessory_selling.html',{'name':ownername})      


def seller_manage_items(request):
    u = request.session['sellername']

    craft_items = craft_selling.objects.filter(owner_name=u)
    accessory_items = accessories_selling.objects.filter(owner_name=u)

    all_items = list(craft_items) + list(accessory_items)
    return render(request, 'seller_manage_items.html', {'all_items': all_items})

def delete_item(request,id):
    data1=craft_selling.objects.get(id=id)

    data1.delete()

    return render(request,'sellerhome.html')


def deletee_itemm(request,id):
    data2= accessories_selling.objects.get(id=id)

    data2.delete()

    return render(request,'sellerhome.html')


def user_profile(request):
    username=request.session['username']
    cr=Reg_user.objects.get(username=username)
    name=cr.name
    username=cr.username
    email=cr.email
    number=cr.number
    return render(request,'user_profile.html',{'name':name,'username':username,'email':email,'number':number})

def seller_profile(request):
    ownername=request.session['sellername']
    cr=Reg_seller.objects.get(username=ownername)
    name=cr.name
    username=cr.username
    email=cr.email
    number=cr.number
    return render(request,'seller_profile.html',{'name':name,'username':username,'email':email,'number':number})

def sellerupdate(request):
    ownername=request.session['sellername']
    cr=Reg_seller.objects.get(username=ownername)
    id=cr.id
    name=cr.name
    username=cr.username
    email=cr.email
    number=cr.number
    return render(request,'sellerupdate.html',{'id':id,'name':name,'username':username,'email':email,'number':number})

def updatesellerprofile(request):
    if request.method =='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        username = request.POST.get('username')
        email=request.POST.get('email') 
        number=request.POST.get('number')

        dt=Reg_seller.objects.get(id=id)
        dt.name=name
        dt.username=username
        dt.email=email
        dt.number=number
        dt.save()
        return render(request, 'sellerhome.html')
    else:
        return render(request, 'sellerupdate.html')
    
def user_update(request):
    username=request.session['username']
    
    cr=Reg_user.objects.get(username=username)
    id=cr.id
    name=cr.name
    username=cr.username
    email=cr.email
    number=cr.number
    address=cr.address
    return render(request,'user_update.html',{'id':id,'name':name,'username':username,'address':address,'email':email,'number':number})

def admin_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        u='admin'
        p='admin'
        if username ==u:
            if password==p:
                return render(request,'admin_home.html')
    return render(request,'admin_login.html')
def admin_home(request):
    return render(request,'admin_home.html')
def admin_user(request):
   data=user.objects.all()
   return render(request,'admin_user.html',{'data':data})
def admin_user_remove(request,id):
    usr=user.objects.get(id=id)
    usr.delete()
    return render(request,'admin_home.html')
def admin_reg_user(request):
   data=Reg_user.objects.all()
   return render(request,'admin_reg_user.html',{'data':data})
def admin_reg_user_remove(request,id):
    usr=Reg_user.objects.get(id=id)
    usr.delete()
    return render(request,'admin_home.html')
def admin_accesories(request):
   data=accessories_selling.objects.all()
   return render(request,'admin_accessories_selling.html',{'data':data})
def admin_accesories_remove(request,id):
    usr=accessories_selling.objects.get(id=id)
    usr.delete()
    return render(request,'admin_home.html')
def admin_seller(request):
   data=Reg_seller.objects.all()
   return render(request,'admin_seller.html',{'data':data})
def admin_seller_remove(request,id):
    usr=Reg_seller.objects.get(id=id)
    usr.delete()
    return render(request,'admin_home.html')
def admin_tutor(request):
   data=Reg_tutor.objects.all()
   return render(request,'admin_reg_tutor.html',{'data':data})
def admin_tutor_remove(request,id):
    usr=Reg_tutor.objects.get(id=id)
    usr.delete()
    return render(request,'admin_home.html')
def admin_craft_selling(request):
   data=craft_selling.objects.all()
   return render(request,'admin_craft_selling.html',{'data':data})
def admin_craft_remove(request,id):
    usr=craft_selling.objects.get(id=id)
    usr.delete()
    return render(request,'admin_home.html')


def tutor_profile(request):
    ownername=request.session['tutorname']
    cr=Reg_tutor.objects.get(username=ownername)
    name=cr.name
    username=cr.username
    address=cr.address
    email=cr.email
    number=cr.number
    return render(request,'tutor_profile.html',{'name':name,'username':username,'address':address,'email':email,'number':number})

def tutor_update(request):
    ownername=request.session['tutorname']
    cr=Reg_tutor.objects.get(username=ownername)
    id = cr.id
    name=cr.name
    username=cr.username
    address=cr.address
    email=cr.email
    number=cr.number
    return render(request,'tutor_update.html',{'id':id,'name':name,'username':username,'address':address,'email':email,'number':number})


def updatetutorprofile(request):
    if request.method =='POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        username = request.POST.get('username')
        address = request.POST.get('address')
        email=request.POST.get('email') 
        number=request.POST.get('number')

        dt=Reg_tutor.objects.get(id=id)
        dt.name=name
        dt.username=username
        dt.address=address
        dt.email=email
        dt.number=number
        dt.save()
        return render(request,'tutorhome.html')
    else:
        return render(request,'tutor_update.html')
# def listitems(request):
#     b=accessories_selling.objects.all()
#     return render(request,'listitems.html',{'x':b})
# def craft_listitems(request):
#     b=craft_selling.objects.all()
#     return render(request,'listitems.html',{'y':b})

def accessory_list_items(request):
    accessory_list_items = accessories_selling.objects.all()
    return render(request, 'accessory_list_items.html', {'items': accessory_list_items})

def craft_list_items(request):
    craft_list_items = craft_selling.objects.all()
    return render(request, 'craftitems.html', {'items': craft_list_items})

def cart(request,id):
    dt=accessories_selling.objects.get(id=id)
    a=dt.item_name
    b=dt.price
    c=dt.image
    d=dt.description
    e=dt.quantity
    username=request.session['username']
    cr=Reg_user.objects.get(username=username)
    username=cr.username
     
    # size=cr.size
    return render(request,'add_cart.html',{'item_name':a,'price':b,'image':c,'description':d,'category':e,'username':username})
def addcart(request):
    if request.method=='POST':
        c= request.POST.get('item_name')
        d=request.POST.get('price')
        e=request.POST.get('description')
        v=int(request.POST.get('quantity'))
        a=request.POST.get('image')
        to=int(d)
        p=int(v)
        amount=int(to*p)
        data=accessories_selling.objects.get(item_name=c)
        qty=int(data.quantity)
        newqty=qty-v
        s=request.session['username']
        cr=Reg_user.objects.get(username=s)
        

        f=cr.username
        if newqty < 0:
            return render(request,'error.html')
        else:
            data.quantity=newqty
            data.save()
            Cart(item_name=c,price=d,description=e,quantity=v,image=a,username=s,totalamount=amount).save()
            return render(request,'userhome.html')
    else:
        return render(request,'add_cart.html')
def cartlist(request):
    username=request.session['username']
    cr=Cart.objects.filter(username=username)
    return render(request,'accessory_cart_list.html',{'a':cr})
def delete1(request,id):
    cr=Cart.objects.get(id=id)
    cr.delete()
    return render(request,'userhome.html')

def craftcart(request,id):
    dt=craft_selling.objects.get(id=id)
    a=dt.item_name
    b=dt.price
    c=dt.image
    d=dt.description
    e=dt.quantity
    username=request.session['username']
    cr=Reg_user.objects.get(username=username)
    username=cr.username
     
    # size=cr.size
    return render(request,'craft_add_cart.html',{'item_name':a,'price':b,'image':c,'description':d,'quantity':e,'username':username})
def addcraftcart(request):
       if request.method=='POST':
        c=request.POST.get('item_name')
        d=request.POST.get('price')
        e=request.POST.get('description')
        v=int(request.POST.get('quantity'))
        a=request.POST.get('image')
        s=request.session['username']
        cr=Reg_user.objects.get(username=s)
        to=int(d)
        p=int(v)
        amount=int(to*p)
        data=craft_selling.objects.get(item_name=c)
        qty=int(data.quantity)
        newqty=qty-v
        s=request.session['username']
        cr=Reg_user.objects.get(username=s)
        

        f=cr.username
        if newqty < 0:
            return render(request,'error.html')
        else:
            data.quantity=newqty
            data.save()

        f=cr.username
        # g=cr.size
        Craftcart(item_name=c,price=d,description=e,quantity=v,image=a,username=f,totalamount=amount).save()
        
        return render(request,'userhome.html')
       else:
         return render(request,'craft_add_cart.html')
def craftcartlist(request):
    username=request.session['username']
    cr=Craftcart.objects.filter(username=username)
    return render(request,'craft_cart_list.html',{'a':cr})
def delete2(request,id):
    cr=Craftcart.objects.get(id=id)
    cr.delete()
    return render(request,'userhome.html')

def payment(request):
    username=request.session['username']
    cr=Cart.objects.filter(username=username)
    totalprice = 0
   
    for i in cr:
     pay(username=i.username, price=i.price).save()
     totalprice += int(i.price)
     i.delete()
   
    totalprice = int(totalprice*100)
    amount=int(totalprice)
    #amount=200
    print('amount is',str(amount))
    currency = 'INR'
    #amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payment.html', context=context)
 
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'pay_success.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'pay_success.html')
            else:
 
                # if signature verification fails.
                return render(request, 'pay_success.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
    
def payment1(request):
    username=request.session['username']
    cr=Craftcart.objects.filter(username=username)
    totalprice = 0
   
    for i in cr:
     pay(username=i.username, price=i.price).save()
     totalprice += int(i.price)
     i.delete()
   
    totalprice = int(totalprice*100)
    amount=int(totalprice)
    #amount=200
    print('amount is',str(amount))
    currency = 'INR'
    #amount = 20000  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler1/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'payment1.html', context=context)
 
@csrf_exempt
def paymenthandler1(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'pay_success1.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'pay_success1.html')
            else:
 
                # if signature verification fails.
                return render(request, 'pay_failed1.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
        
        
class VideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Access the session variable 'tutorname'
        username = kwargs.pop('username', None)
        super().__init__(*args, **kwargs)
        # Set required attribute to False for video_link and video_file fields
        self.fields['video_link'].required = False
        self.fields['video_file'].required = False
        # Assign the value of 'tutorname' to the 'username' field of the form
        if username:
            self.fields['username'].initial = username

    class Meta:
        model = Video
        fields = ['category', 'title', 'video_link', 'video_file', 'username']

def video_list(request):
    username=request.session['tutorname']
    videos = Video.objects.filter(username=username)
    return render(request, 'video_list.html', {'videos': videos})

def add_video(request):
    username = request.session.get('tutorname')
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES,username=username)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm(username=username)
    return render(request, 'add_edit_video.html', {'form': form, 'action': 'Add'})

def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm(instance=video)
    return render(request, 'add_edit_video.html', {'form': form, 'action': 'Edit', 'video': video})


def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    return redirect('video_list')      
# views.py

from django.shortcuts import render
from .models import Video

def user_video_list(request):
    videos = Video.objects.all()
    return render(request, 'user_video_list.html', {'videos': videos})
from django import forms
from django.shortcuts import render, get_object_or_404, redirect

class ItemEditForm(forms.ModelForm):
    class Meta:
        model = craft_selling
        fields = ['item_name', 'category', 'price', 'image']

def edit_item(request, item_id):
    item = get_object_or_404(craft_selling, id=item_id)
    form = ItemEditForm(instance=item)

    if request.method == 'POST':
        form = ItemEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('seller_manage_items')

    return render(request, 'edit_item.html', {'item': item, 'form': form, 'action': 'Edit'})
class AcceriosEditForm(forms.ModelForm):
    class Meta:
        model = accessories_selling
        fields = ['item_name', 'category', 'price', 'image']
def edit_accerios(request, item_id):
    item = get_object_or_404(accessories_selling, id=item_id)
    form = AcceriosEditForm(instance=item)

    if request.method == 'POST':
        form = AcceriosEditForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('seller_manage_items')  # Adjust the URL name accordingly

    return render(request, 'edit_accerios.html', {'item': item, 'form': form, 'action': 'Edit'})
def craftdeletee_itemm(request,id):
    data2= craft_selling.objects.get(id=id)

    data2.delete()

    return render(request,'sellerhome.html')
