from django.urls import path
from .views import RegisterUserView, UserView, AllUsersView

urlpatterns = [
    path('', AllUsersView.as_view()),
    path('user/', UserView.as_view()),
    path('register/', RegisterUserView.as_view()),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
