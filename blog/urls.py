from django.urls import path
from blog.views import home,postdetails,register,profile,contact,index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",home,name="home" ),
    path('register',register,name="register"),
    path('index',index,name="index"),
    path('login', auth_views.LoginView.as_view(),name="login" ),
    path('logout', auth_views.LogoutView.as_view(),name="logout" ),
    path('profile',profile,name="profile"),
    path('contact',contact,name="contact"),
    path("<slug:slug>",postdetails,name="postdetails")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)