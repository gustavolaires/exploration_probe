from django.urls import path
from .views import GetCoordinatesView, MoveView, ReturnToInicialCoordinatesView

urlpatterns = [
    path('coordinate/', GetCoordinatesView.as_view()),
    path('move/', MoveView.as_view()),
    path('reset/', ReturnToInicialCoordinatesView.as_view()),
]
