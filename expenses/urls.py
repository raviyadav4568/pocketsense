from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ExpenseViewSet, PaymentViewSet, ConcernViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'concerns', ConcernViewSet)

urlpatterns = [

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('pocketsense/', include(router.urls)),
]
