from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.apioverview, name="api_overview"),
    path("widget_list/", views.widgetlist, name="widget_list"),
    path("widget_create/", views.widgetcreate, name="widget_create"),
    path("widget_delete/<str:pk>", views.widgetdelete, name="widget_delete")
]