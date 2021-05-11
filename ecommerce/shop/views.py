
from django.shortcuts import render
from django.conf import settings

import os
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request):
 

    context={}
    products = product.objects.all()
    context['products'] = products
    return render(request, "shop/index2.html",context=context)

def addproduct(request):
    if request.method == 'GET':
        
        tops = ["Furniture","Electronics"]

        context = {}
      
        context['tops'] = tops
        return render(request,'shop/addproduct.html',context= context)

    if request.method == 'POST':
        data = request.POST
           
        product1 = product()


        product1.productaname = data.get('productname')
        product1.producttopping = data.get('toppings')
        product1.producttype = data.get('product_type')
        product1.productdesc = data.get('productdesc')
        product1.productqty = data.get('product_qty')
        product1.productprice = data.get('product_price')
        if 'image_logo' in request.FILES:

            image = request.FILES.get('image_logo')
            img_name = f"{product1.id}.png"
            if image.name.endswith('.png') or image.name.endswith('.PNG'):


                if os.path.exists(os.path.join(settings.MEDIA_ROOT,"ProductImages",img_name)):
                    os.remove(os.path.join(settings.MEDIA_ROOT,"ProductImages", img_name))

                image.name = img_name
                product1.product_logo_url = image
            else:
                return HttpResponse("Please upload only a PNG File")
        product1.save()
        return redirect('home')

    return render(request,"shop/addpizza.html")

def deleteproduct(request):
    if request.method=='GET':
        todeleteid = request.GET['productid']
        todelete = product.objects.get(id=todeleteid)
        todelete.delete()
        return HttpResponse("deleted successfully")
    return HttpResponse("error")

def editproduct(request,editid):

    toeditobj = product.objects.get(id = editid)
    context = {}
    context['product'] = toeditobj
    return render(request,"shop/addproduct.html",context=context)
        