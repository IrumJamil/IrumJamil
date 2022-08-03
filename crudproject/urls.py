
from django.contrib import admin
from django.urls import path
from add import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base,name='home'),
    path('delete/<int:id>/', views.delete,name='deletedata'),
    path('<int:id>/', views.update,name='updatedata'),
]
