from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name ='login'),
    path('logout/', views.user_logout, name ='logout'),
    path('signup/', views.signup, name ='signup'),
    path('index/', views.index, name ='index'),
    path('', views.index, name ='index'),
    path('profile/', views.profile, name ='profile'),
    path('suggestion/', views.suggestion, name ='suggestion'),
    path('update/<int:id>/', views.update, name ='update'),
    path('setting/', views.setting, name ='setting'),
    path('render_/', views.rendertosetting, name ='render_'),
    path('verify/<slug:token>/', views.account_verify, name ='verify'),
    path('like', views.like, name='like'),
    path('postdelete', views.postdelete, name='postdelete'),
    path('profile_post_delete', views.profile_post_delete, name='profile_post_delete'),
    path('comment', views.comment, name='comment'),
]
