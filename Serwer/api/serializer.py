from rest_framework import serializers

from api.models import Grade


class GradeSerializer(serializers.ModelSerializer):
    grade = serializers.DecimalField(max_digits=3, decimal_places=2)
    description = serializers.CharField()
    subject = serializers.CharField()

    class Meta:
        model = Grade
        fields = '__all__'