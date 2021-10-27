from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:pk>', delete, name='delete'),
    path('edit/<int:pk>', edit, name='edit'),
    path("api-create/", CreateTask.as_view(), name="ac"),
    path("api-list/", RetrieveTasks.as_view(), name="raa"),
    path("api-update/<id>/", UpdateTodo.as_view(), name="upc"),
    path("api-delete/<id>/", Delete.as_view(), name="upi")
]

