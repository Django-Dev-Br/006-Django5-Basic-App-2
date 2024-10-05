from django.urls import path
from .views import example_view  # Importa a view `example_view` do arquivo `views.py` do app

urlpatterns = [
    path('', example_view),  # Define a rota principal ('/') e associa à função `example_view`
]
