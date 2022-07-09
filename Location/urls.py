from . import views
from django.urls import path, include, re_path

urlpatterns = [
    path('<int:country_id>', views.Country_page, name='Country_page'),
    path('regions/<str:region_code>', views.region_page, name='region_page'),
]