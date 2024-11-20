from django.urls import path
from .views import BotConfigView, BotRunView

urlpatterns = [
    path('configs/', BotConfigView.as_view()),
    path('configs/<int:pk>/run/', BotRunView.as_view()),
]
