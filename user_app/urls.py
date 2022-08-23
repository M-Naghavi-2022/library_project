from django.urls import path

from .views import MemberProfileView, index, logout, SignUp, Login

urlpatterns = [
    path('', index, name="home"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('profile/', MemberProfileView.as_view() , name="profile"),
]