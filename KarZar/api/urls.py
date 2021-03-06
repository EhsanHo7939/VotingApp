from django.urls import path, include
from . import views
# from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name="QuestionList"),
    path('questions/<str:pk>/', views.QuestionDetail.as_view(), name="QuestionDetail"),
    path('votes/', views.VoteList.as_view(), name="VoteList"),
    path('votes/<str:pk>/', views.VoteDetail.as_view(), name="VoteDetail"),
    path('users/', views.UserList.as_view(), name="UserList"),
    path('users/<str:pk>/', views.UserDetail.as_view(), name="UserDetail"),

    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    path('auth/', include('dj_rest_auth.urls'), name="authentication"),
    path('auth/registration/', include('dj_rest_auth.registration.urls'), name="registration"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
