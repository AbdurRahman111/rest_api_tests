from rest_framework import serializers


from .models import staff_info, staff_salary, staff_ratings


class staff_info_serializers(serializers.ModelSerializer):
    class Meta:
        model=staff_info
        fields="__all__"

class staff_salary_serializers(serializers.ModelSerializer):
    staff = staff_info_serializers()
    class Meta:
        model=staff_salary
        fields="__all__"


class staff_ratings_serializers(serializers.ModelSerializer):
    staff = staff_info_serializers()
    class Meta:
        model=staff_ratings
        fields="__all__"
