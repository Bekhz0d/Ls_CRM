from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('groups', views.TeachGroupViewSet, basename='groups')
router.register('students', views.StudentsViewSet, basename='students')


urlpatterns = [
    path('login/token/', views.TokenObtainPairView.as_view(), name='login'),
    path('signup/token/', views.UserRegistrationView.as_view(), name='signup'),
]

urlpatterns += router.urls
