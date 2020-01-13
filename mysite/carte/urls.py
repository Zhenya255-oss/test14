from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('<str:name>/subscribe/', views.subscribe, name='subscribe'),
    path('account/<str:searched_user_profile>', views.userpage, name='account'),
    path('account/<str:user>/way', views.way, name='myway'),
    path('account/<str:user>/consultations', views.consultations, name='consultations'),
    path('account/<str:user>/influencers', views.influencers, name='myinfluencers'),
    path('account/<str:user>/edit', views.edit, name='changeinfo'),
    path('account/<str:user>/notes', views.notes, name='notes'),
    path('account/likepost/<str:user>/<int:post_id>', views.likepost, name='likepost'),

]

