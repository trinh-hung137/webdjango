from django import urls
from django.urls import path 
from . import views 
# tạo danh sách URL
urlpatterns = [
    # các đường dẫn liên quan đến các chế độ xem
    path('', views.store, name = "store"),
    path('cart/', views.cart , name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('process_order/', views.processOrder, name = "process_order"),
    path('detail/', views.detail, name="detail"),
    path('about/', views.about, name="about"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]
