from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"), 
	path('admin/', views.cart, name="admin"), 

	path('update_item/', views.updateItem, name="update_item"),
 

]