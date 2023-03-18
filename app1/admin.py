from django.contrib import admin
from .models import staff_info, staff_salary, staff_ratings
# Register your models here.


admin.site.register(staff_info),
admin.site.register(staff_salary)
admin.site.register(staff_ratings)