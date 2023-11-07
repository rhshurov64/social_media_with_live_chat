from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name ='login'),
    path('logout/', views.user_logout, name ='logout'),
    path('signup/', views.signup, name ='signup'),
    path('index/', views.index, name ='index'),
    path('', views.index, name ='index'),
    path('profile/<int:id>/', views.profile, name ='profile'),
    path('blocklist/<int:bid>/', views.blocklist, name ='blocklist'),
    path('suggestion/', views.suggestion, name ='suggestion'),
    path('update/<int:id>/', views.update, name ='update'),
    path('name_edit/<int:id>/', views.name_edit, name ='name_edit'),
    path('setting/', views.setting, name ='setting'),
    path('render_/', views.rendertosetting, name ='render_'),
    path('verify/<slug:token>/', views.account_verify, name ='verify'),
    path('like', views.like, name='like'),
    path('postedit/<int:id>/', views.postedit, name='postedit'),
    path('commentedit/<int:id>/', views.commentedit, name='commentedit'),
    path('replayedit/<int:id>/', views.replayedit, name='replayedit'),
    path('postdelete', views.postdelete, name='postdelete'),
    path('profile_post_delete', views.profile_post_delete, name='profile_post_delete'),
    path('comment_delete', views.comment_delete, name='comment_delete'),
    path('replay_delete', views.replay_delete, name='replay_delete'),
    path('comment/<int:id>', views.comment, name='comment'),
    path('comment/show_comment/<int:id>/', views.show_comment, name='show_comment'),
    path('show_replay/<int:pid>/<int:cid>/', views.show_replay, name='show_replay'),
    path('showblocklist/', views.showblocklist, name='showblocklist'),
    path('unblock/<int:block_user_id>/', views.unblock, name='unblock'),
    path('download_image/<int:image_id>/', views.download_image, name='download_image'),
    path('suggesions_search/', views.suggesions_search, name='suggesions_search'),
]


