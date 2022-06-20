from django.contrib import admin
from django.urls import path,include
from blog_arquitectura.views import index,about,login_view,logout_view,register_view,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('app_blog/', include('app_blog.urls')),
    path('app_blog/about/',about ,name = 'about'),
    path('app_blog/contact/',contact ,name = 'contact'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
]


