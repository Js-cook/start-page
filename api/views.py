from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Widget
from .serializers import WidgetSerializer

# Create your views here.
@api_view(["GET"])
def apioverview(request):
  api_urls = {
    "Create": "/widget_create/",
    "List": "/widget_list/",
    "Delete": "/widget_delete/<str:pk>"
  }
  return Response(api_urls)

@api_view(["POST"])
def widgetcreate(request):
  serializer = WidgetSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(["GET"])
def widgetlist(request):
  widgets = Widget.objects.all()
  serializer = WidgetSerializer(widgets, many=True)
  return Response(serializer.data)

@api_view(["DELETE"])
def widgetdelete(request, pk):
  widget = Widget.objects.get(id=pk)
  widget.delete()
  return Response("Widget Removed")