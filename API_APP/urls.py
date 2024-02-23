from django.urls import path
from API_APP import views

urlpatterns = [
    
    path('API/Resume/',views.ProfileView.as_view(), name='profile_view'),
      path('API/Resume/<int:pk>/',views.ProfileView.as_view(), name='profile_view'),
    # path('API-Resume-Update/<int:pk>/',views.ProfileView.as_view()),
    # path('API-list/',views.ProfileView.as_view(),name='list'),


]