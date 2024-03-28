from django.contrib import admin
from django.urls import path
from Gov import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mps/', views.mps_list),
    path('mps/<str:constituency>/', views.search_mp_by_constituency),
    path('senators/', views.senators_list),
    path('senators/<str:county>/', views.search_senator_by_county),
    path('governors/', views.governors_list),
    path('governors/<str:county>/', views.search_governor_by_county),
    path('mcas/', views.mcas_list),
    path('mcas/<str:ward>/', views.search_mca_by_ward)
]

urlpatterns = format_suffix_patterns(urlpatterns)
