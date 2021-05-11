from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('deleteproduct',views.deleteproduct,name='deleteproduct'),
    path('editproduct/<int:editid>/',views.editproduct,name='editproduct'),
]