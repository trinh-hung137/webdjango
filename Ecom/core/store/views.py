from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse # nhập phản hồi JSON để sử dụng cho chế độ xem
import json
import datetime
from django.contrib.auth.decorators import login_required
from.models import *    # import hàm để nhập tất cả các class trong model
from .forms import CreateUserForm
# Create your views here.
@login_required(login_url='login')
#chế độ xem cửa hàng
def store(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    products = Product.objects.all()    # nhận tất cả các sản phẩm
    item_name=request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        products=products.filter(name__icontains=item_name)
    context = {'products': products, 'cartItems': cartItems }
    return render(request, 'store/store.html', context)

@login_required(login_url='login')
# chế độ xem trang liên hệ
def about(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/about.html', context)

@login_required(login_url='login')
# chế độ xem chi tiết sản phẩm trong giỏ hàng
def detail(request):  
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/detail.html', context)

@login_required(login_url='login')
# chế độ xem trang giỏ hàng
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

@login_required(login_url='login')
# chế độ xem trang thanh toán
def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {'items': items, 'order': order,'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

@login_required(login_url='login')
# cập nhật giỏ hàng
def updateItem(request):
    data = json.loads(request.body)     # phân tích dữ liệu chuyển về dạng chuỗi
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

@login_required(login_url='login')
# chế độ đặt hàng
def processOrder(request):          # hàm trả về phản hồi JSON nói khoản thanh toán đã được gửi
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
    
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                zipcode = data['shipping']['zipcode'],
                phone = data['shipping']['phone'],
            )
        
    else:
        print('User is not logged in...')

    return JsonResponse('Payment complete!...', safe=False)
# chế độ đăng ký tài khoản
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'store/register.html', context)
# chế độ đăng nhập
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('store')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'store/login.html', context)
# chế độ thoát tài khoản
def logoutUser(request):
	logout(request)
	return redirect('login')
