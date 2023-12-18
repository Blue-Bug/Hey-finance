from django.urls import path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register("board",BoardViewSet)

app_name = "board"
urlpatterns = [
    path("",views.BoardListAPIView.as_view(), name="board-list"),
    path("<int:pk>/",views.BoardRetrieveAPIView.as_view(), name="board-retrieve"),
    path("new/",views.BoardCreateAPIView.as_view(),name="board-create"),
    path("<int:pk>/update/",views.BoardUpdateAPIView.as_view(),name="board-update"),
    path("<int:pk>/delete/",views.BoardDeleteAPIView.as_view(),name="board-delete"),
    
    
    
]