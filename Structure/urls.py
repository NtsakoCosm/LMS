from django.urls import path
from . import views
from .views import StudentlistView
urlpatterns = [
    path('',StudentlistView.as_view(),name='home'),
    path('Profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('module_guide/<str:module>',views.module_guide,name="module_guide")

]
