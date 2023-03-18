from django.urls import path
from . import views

urlpatterns = [
    path('staff_info_see/', views.staff_info_see, name="staff_info_see"),
    path('staff_create/', views.staff_create, name="staff_create"),
    path('staff_update/', views.staff_update, name="staff_update"),
    path('see_all_staffs/', views.see_all_staffs, name="see_all_staffs"),
    path('one_salary/', views.one_salary, name="one_salary"),
    path('show_multiple_results_from_database/', views.show_multiple_results_from_database, name="show_multiple_results_from_database"),
]