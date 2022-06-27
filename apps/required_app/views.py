from django.shortcuts import render
from rest_framework import viewsets, serializers

from apps.required_app.models import Segment


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = "__all__"


class SegmentViewSet(viewsets.ModelViewSet):
    serializer_class = SegmentSerializer

    def get_queryset(self):
        return Segment.objects.all()
