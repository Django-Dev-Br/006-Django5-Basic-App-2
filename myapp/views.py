from django.http import HttpResponse  # Importa a classe HttpResponse, responsável por retornar respostas HTTP

def example_view(request):
    return HttpResponse("app up and running properly")  # Retorna uma mensagem indicando que o app está funcionando corretamente
