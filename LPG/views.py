


from django.db.models import OuterRef, Subquery
from datetime import datetime, timedelta
from django.db.models.functions import TruncMonth
from itertools import count

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login

from django.db.models import Max,Min,Avg,Count,Sum
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import Group, Permission

from django.http import HttpResponse




from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from generalstore.models import gasentry, gasondemand,category
from generalstore .forms import gasdemand, newentry




def base(request):
    return render(request,'base.html')

def sindex(request):
    gas=gasentry.gasentrymanager.all()
    total=gas.aggregate(totalgas=Sum('quantity'))['totalgas']
    return render(request,'supplier_dashboard/index.html',{'gas':total})

def landingheader(request):
    # signupform = SignUpForm()
   
    f = UserCreationForm()
    gascategory=category.objects.all()
    print(gascategory)
 
    return render(request, 'landingheader.html', {'form':f,'cate':gascategory})


    
def bookedgas(request):
    
   
    if 'bookid' not in request.session:
        return render(request,'customer_dash/booking.html')
      
    else:
        gas=gasentry.gasentrymanager.get(id=request.session['bookid'])
        return render(request,'customer_dash/booking.html',{'id':gas})
        

@login_required
def customerdashboard(request):
    notification=gasondemand.objects.filter(Customer_name=request.user,status='accepted').count()
   
    return render(request,'customer_dash/body.html',{'notification':notification})


def gasordered(request):
    if request.method=='POST':
        suppliername=request.POST.get('supplier_name')
        customername=request.POST.get('customer_name')
        customeraddress=request.POST.get('address')
        customercontact=request.POST.get('customer_contact')
        requiredcategory=request.POST.get('category')
        requiredquantity=request.POST.get('quantity')
        getby=request.POST.get('getby')      
     
        gasordered=gasondemand(Customer_name=customername, customer_address=customeraddress,required_quantity=requiredquantity,gas_category=requiredcategory,customer_contact=customercontact,supplier=suppliername,getby=getby)
        gasordered.save();
        
        
        
        return redirect(customerdashboard)
    else:
        return render(request,'customer_dash/booking.html')

def status(request):
    if request.method=='POST':
        id=request.POST.get('id')
        print(id)
        status=request.POST.get('status')
        print(status)
        gasondemand.objects.filter(id=id).update(status=status)
        
        messages.success(request,'action performed successfully')
        return redirect(supplierdashboard)



    

def bookgas(request):
   
    bookid=request.POST.get('id')
    request.session['bookid']=bookid
    print(bookid)
    return redirect(userlogin)
 


    

def profileinfo(request):
    return render(request,'customer_dash/profileinfo.html')
    
    
@login_required
def supplierdashboard(request):
    allgas=gasentry.gasentrymanager.filter(supplier=request.user)
    notification=gasondemand.objects.filter(supplier=request.user, status='pending')
    accepted=gasondemand.objects.filter(supplier=request.user, status='accepted').count()
    rejected=gasondemand.objects.filter(supplier=request.user, status='rejected').count()
    pending=gasondemand.objects.filter(supplier=request.user, status='pending').count()
    readytosold=gasondemand.objects.filter(supplier=request.user, status='accepted')
    sold=readytosold.aggregate(total=Sum('required_quantity'))['total']
    total=gasentry.gasentrymanager.filter(supplier=request.user).aggregate(tot=Sum('quantity'))['tot']
    category=gasondemand.objects.filter(supplier=request.user, status='accepted',created_at__gt=datetime.now() - timedelta(days=1)).distinct()
    sales_category=gasondemand.objects.filter(supplier=request.user, status='accepted',created_at__gt=datetime.now() - timedelta(days=2)).annotate(sum=Sum('required_quantity'))
    
   

    
   
   
    algodata=gasondemand.objects.filter(supplier=request.user,status='accepted',created_at__gt=datetime.now() - timedelta(days=2)).aggregate(sum=Sum('required_quantity'))['sum']
    # print(algodata)
    # predtict=int(algodata/2)
    # print(predtict)
    # out_of_stock=int(total/predtict)
    
    # print(out_of_stock) 
    # if out_of_stock <=5:
    #     messages.success(request,'you have less than five days for stock clearence')
    # return render(request,)
        
    # ,created_at__gt=datetime.now() - timedelta(days=6)
    # time_of_sold=gasondemand.objects.filter(supplier=request.user, status='accepted').values('created_at__date').order_by('created_at__date').annotate(sum=Sum('required_quantity'))
    # predict=time_of_sold.aggregate(total_quantity=Sum('required_quantity'))['total_quantity']
    # predict = gasondemand.objects.annotate(week=TruncMonth('created_at')).values('week').annotate(total_amount=Sum('required_quantity'))
   
    # top_seven_days_data=gasondemand.objects.filter(supplier=request.user, status='accepted',created_at__gt=datetime.now() + timedelta(days=7))
    # forecast=top_seven_days_data.aggregate(averagedata=Sum('required_quantity'))['averagedata']
    
   
    totalgas=allgas.aggregate(totalgas=Sum('quantity'))['totalgas']
    # remaining=totalgas- sold

    gas=allgas.filter(supplier=request.user.id,created_at__gt=datetime.now() - timedelta(days=30))
    return render(request,'supplierdash/body.html',{'newentry':newentry,'alldata':gas,'totalgas':totalgas,'notification':notification,'accepted':accepted,'rejected':rejected,'pending':pending,'sold':sold,'total':total,'category':category})
    


def search(request):

    address=request.POST.get('address')
    cate=request.POST.get('category')
    gascategory=gasentry.gasentrymanager.values_list('category',flat=True).distinct() 
    # category__icontains=category,
                
    data=gasentry.gasentrymanager.filter(category=cate,complete_firm_address__icontains=address)
    gascategory=category.objects.all()
    print(address,category)
    # fill=gasdemand()
    f = UserCreationForm()
    
    # print(query)
    # return HttpResponse()
    
    return render(request,'landingheader.html',{'data':data,'form':f,'cate': gascategory})
    # return HttpResponse('hi')

def body(request):
    return render(request,'supplierdash/body.html')

def supplierin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        supplier=auth.authenticate(username=username, password=password)
        if supplier is not None and supplier.is_staff==True and supplier.is_superuser==False:
            messages.success(request,'welcome User')
            login(request,supplier)
            return redirect(supplierdashboard)
        else:
            messages.success(request, 'username or password invalid')
            return redirect(supplierlogin)
    else:
     return render(request,'supplier/login.html')

def supplierout(request):
    logout(request)
    return redirect(supplierin);



        


        
        



   

def customerlogin(request):
   
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
     
        
        
        user=auth.authenticate(request,username=username, password=password)


        if user is not None and user.is_staff==False and user.is_superuser==False:          
            login(request,user)
            
            return redirect(customerdashboard) 
           
        else:
            messages.success(request,'Username or password incorrect ! Please get registered')
            return redirect(landingheader)
    else:
        return redirect(landingheader)

def customerlogout(request):
    logout(request)
    return redirect(landingheader);


def userlogin(request):
    
    return render(request,'customer_dash/userlogin.html' )
def supplierlogin(request):
    return render(request,'supplier/login.html' )

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
     
        if f.is_valid(): 
           
        # return HttpResponse('hre we are') 
        # email=form.cleaned_data.get('email')
        # print(email)
        # username=form.cleaned_data.get('username')
        # print(username)
            # form.save()
            # return redirect(landing)
           
            # group=Group.objects.get(name='customer')
                  
            # user.groups.add(group)
            

           
            

            # if User.objects.filter(email=email).exists():
            #     messages.success(request, 'email  is already taken')
            #     return redirect(landing)

            # elif User.objects.filter(username=username).exists():
            #     messages.success(request,'contact  is already taken' )
            #     return redirect(landing)
                
            # else:
            
           
            f.save()
            messages.success(request,'registered successfully') 
            return redirect(landingheader)
            
            # return redirect(landing)
def report(request):
  
   
   time_of_sold=gasondemand.objects.filter(supplier=request.user, status='accepted').values('created_at__date').order_by('created_at__date').annotate(sum=Sum('required_quantity')).annotate(category=Count(('gas_category'),distinct=True))
 
   return render(request,'supplierdash/report.html',{'time_of_sold':time_of_sold})

# def category(request):
#     return HttpResponse("hi this is me")
    # selected_category=gasondemand.objects.filter(id=items.id)
  

   
  

        

   

    
    
    




   


def entry(request):
    if request.method=="POST":
       f = newentry(request.POST)
       if f.is_valid():
            form= f.save(commit=False)
            form.supplier = request.user
            form.save()
            messages.success(request, 'data inserted successfully')
            return redirect(supplierdashboard)
        # return render(request,'supplier_dashboard/index.html',{'msg':msg})
    else:
        messages.success(request, 'data cant be inserted')
        return redirect (supplierdashboard)
    
def viewdata(request):
    
    retrive=gasentry.objects.all()
    return render(request,'supplier_dashboard/table.html',{'data':retrive})






def gas_delete(request, pk):
    
    gas=gasentry.gasentrymanager.get(id=pk)
    gas.delete()
    return redirect('supplierdashboard')
def gas_update(request,pk):
    
    gas=gasentry.gasentrymanager.get(id=pk)
    form1=newentry(request.POST or None ,instance=gas)
    
    
    if form1.is_valid():
        form1.save()
        messages.success(request,"data updated successfully")
        return redirect('supplierdashboard')
    return render(request,'supplierdash/update.html',{'toupdate':form1})
    
   
        
   

        
   
        
