from django.db import models

# Create your models here.


class staff_info(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    adsd = models.CharField(max_length=255)


class staff_salary(models.Model):
    staff = models.ForeignKey(staff_info, on_delete=models.CASCADE)
    Salary = models.CharField(max_length=255)


class staff_ratings(models.Model):
    staff = models.ForeignKey(staff_info, on_delete=models.CASCADE)
    rating = models.CharField(max_length=255)