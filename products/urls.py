from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(), name='index'),
    path('upvote/', views.upvote, name='upvote'),
    path('create/', views.ProductCreate.as_view(), name='create'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='detail'),
    # path('<str:username>/', views.UserProducts.as_view(), name='userproducts'),
    path('<int:user_id>/<str:username>/', views.user_products,name='userproducts')
]