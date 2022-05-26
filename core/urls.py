from django.urls import path
from .views import *

app_name = 'core'


urlpatterns = [
    path('', IndexView, name='index'),
    path('parent_dashboard/', ParentDashboard, name='parent-dashboard'),
    path('parent-profile-update/', parent_profile_settings, name='parent-profile-update'),
    path('parent-dashboard/change-password/', dashboard_change_password, name='dashboard-change-password'),
    path('create-child/', create_child, name='create-child'),
    path('child-profile/<uuid>/', child_profile, name='child-profile'),
    path('child-profile-update/<uuid>/', child_profile_update, name='child-profile-update'),

    path('doctor-dashboard/', doctor_dashboard, name='doctor-dashboard'),
]
