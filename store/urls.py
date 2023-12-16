from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name = "home"),
    path('dashboard', dashboard, name = "dashboard"),
    path('products_view', products_view, name = "products_view"),
    path('view_product', view_product, name = "view_product"),
    path('profile', profile, name = "profile"),
    path('signin', signin, name = "signin"),
    path('signout', signout, name = "signout"),
    path('profile', profile, name='profile'),
    path('signout', signout, name = "signout"),
    path("register", register, name="register"),
    path("product/<str:pk>", product, name="product"),
    path("delete/<str:pk>", delete, name="delete"),
    path("add_product", add_product, name="add_product"),
    path("<store>/", store_category, name="store_category"),
    path("categories/<category>/", product_category, name="product_category"),
    path("update_product/<str:pk>", UpdateProduct.as_view(), name ="update_product" ),
    path("delete_product/<str:pk>", delete_product, name ="delete_product" ),

]
