from django.shortcuts import render, redirect
from .models import product
import os

# Create your views here.
def index(request):
    return render(request,'products.html')

def add(request):
  if request.method=='POST':
        p=request.POST['name']
        q=request.POST['price']
        r=request.POST['quantity']
                                        #image=request.FILES['file']   another way
        img=request.FILES.get('file')
        db=product(product_name=p,price=q,quantity=r,image=img)
        db.save()
        return redirect('details')
  
def details(request):
    prd=product.objects.all()
    return render(request,'details.html',{'prs':prd})

def edit(request,pk):
    pd=product.objects.get(id=pk) 
    return render(request,'update.html',{'ps':pd})

def update(request,pk):
    if request.method=='POST':
        prds = product.objects.get(id=pk)
        prds.product_name = request.POST.get('pname')
        prds.price = request.POST.get('pprice')
        prds.quantity = request.POST.get('pquantity')
        if len(request.FILES)!=0:
            if len(prds.image)>0:
                os.remove(prds.image.path)
            prds.image = request.FILES.get('file')
        prds.save()
        return redirect('details')
    return render(request, 'update.html')

def delete(request,pk):
    d=product.objects.get(id=pk)
    d.delete()
    return redirect('details')

def back(request):
    return render(request,'products.html')