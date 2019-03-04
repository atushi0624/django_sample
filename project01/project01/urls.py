"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static
from app01.views import App01ListView,App01CreateView,App01DetailView,App01UpdateView
from myapp.views import FoodListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', App01ListView.as_view(), name="index"),
    path('create/', App01CreateView.as_view(), name="create"),
    path('detail/<int:pk>', App01DetailView.as_view(), name="detail"),
    path('update/<int:pk>', App01UpdateView.as_view(), name="update"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
