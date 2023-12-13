from django.urls import path,include
from .views import ProfileView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('formvalid',ProfileView)

urlpatterns = [
    path('',include(router.urls))
]