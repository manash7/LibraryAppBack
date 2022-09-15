from posixpath import basename
from django.urls import path
from LibraryApp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)




urlpatterns=[
    # path('users',views.usersApi),
    path('books/',views.ListBooks.as_view()),
    path('books/<int:pk>',views.ListBooks.as_view(),name='patch'),
    path('register/',views.RegisterUser.as_view()),
    path('login/',views.LoginUser.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

