from django.urls import path, include
from oferta import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', views.RegistrationView.as_view(), name='registration'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('accounts/profile/zmien/', views.UserChangeView.as_view(), name='change_user'),
    #ADS
    path('ads/select_kind/', views.AdKindSelectView.as_view(), name='choose_ad_type'),
    path('ads/create/driver/', views.DriverAdCreateView.as_view(), name='create_driver_ad'),
    path('ads/create/passenger/', views.PassengerAdCreateView.as_view(), name='create_passenger_ad'),
    path('ads/', views.ActiveAdsList.as_view(), name='ads-list'),
    path('my-ads/', views.MyAdsList.as_view(), name='my-ads-list'),
    path('ads/<int:pk>/', views.AdUpdateView.as_view(), name='update_ad'),
    path('ads/<int:pk>/delete/', views.AdDeleteView.as_view(), name='delete_ad'),
    path('ads/<int:pk>/complete/', views.AdCompleteView.as_view(), name='complete_ad'),
    # SUBSCRIPTION
    path('ads/<int:pk>/subscribe/', views.CreateSubscribeView.as_view(), name='subscribe_to_ad'),
    path('subs/<int:pk>/confirm/', views.ConfirmSubscribe.as_view(), name='confirm_subscribe'),
    path('subs/<int:pk>/reject/', views.RejectSubscribe.as_view(), name='reject_subscribe'),
    path('subs/<int:pk>/cancel/', views.CancelSubscribe.as_view(), name='cancel_subscribe'),
]
