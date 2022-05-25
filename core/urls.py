from django.urls import path
from .views import *

app_name = 'core'


urlpatterns = [
    path('', IndexView, name='index'),
    path('parent_dashboard/', ParentDashboard, name='parent-dashboard'),
    path('parent-profile-update/', parent_profile_settings, name='parent-profile-update')
]
