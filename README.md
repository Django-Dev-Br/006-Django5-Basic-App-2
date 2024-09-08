
# 006 Django 4 Basic App 2 (Import URLconf)

### O que é um App Django?

Um app no Django é uma aplicação web que faz algo — um grupo de modelos, views, templates, e outras partes lógicas que tratam de um problema específico ou funcionalidade. Apps são projetados para serem reutilizáveis, plugáveis e independentes, facilitando a manutenção e a extensão de funcionalidades.

## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12 com PIP e venv**

- **No [repositório 001](https://github.com/Django-Dev-Br/001-django4-basic-project) há explicações sobre PIP e venv**
  
  [Baixar Python 3.12](https://www.python.org/downloads/release/python-3122/)

  Confira o vídeo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual):  
  [![Watch the video](https://img.youtube.com/vi/eetDeQrv0Rs/0.jpg)](https://youtu.be/eetDeQrv0Rs)

- **Virtualenv**

  Para instalar o pacote `virtualenv` no Python, utilize os seguintes comandos:

  - **Linux**:
    ```bash
    python3 -m pip install virtualenv
    ```

  - **Windows**:
    ```bash
    python -m pip install virtualenv
    ```

### Passos para Executar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Django-Dev-Br/005-Django-4-Basic-App-2.git
    ```

2. **Crie um ambiente virtual**:
   
    **Windows**
    ```bash
     python -m venv myvenv  
    ```
   **Linux**
    ```bash
     python3 -m venv myvenv  
    ```

3. **Ative o ambiente virtual criado**:
   
    **Windows**
    ```bash
    myvenv\Scripts\activate  
    ```

   **Linux**
    ```bash
    source myvenv/bin/activate  
    ```

4. **Instale o Django**:
   
    ```python
    pip install django==4.2.15
    ```

5.**Acesse a pasta do repositório**:

    ```bash
    cd 005-Django-4-Basic-App-2
    ```
    
6. **Execute o servidor de desenvolvimento**:
   
    ```python
    python manage.py runserver
    ```

8. **Acesse a View no Navegador**:

   Abra o navegador e vá para o endereço [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver a mensagem:

   ```
   app up and running properly
   ```


### Como Criar um Novo App Django

Para criar um novo app em um projeto Django, use o seguinte comando:

```python
python manage.py startapp nome_do_app
```

### Sobre Nosso Treinamento Prático-Profissional com projeto real para iniciantes e avançados em web DevOps Full-stack com Python, Django, Bootstrap e Linux.

[Django Developers Brasil - Aprenda programando enquanto programa aprendendo!](https://django.dev.br/)

Nosso treinamento oferece uma experiência prática de aprendizado de programação, adequada tanto para iniciantes quanto para desenvolvedores avançados. Você participará de um projeto real de desenvolvimento de software em um ambiente corporativo autêntico, onde pessoas com diferentes níveis de conhecimento irão colaborar, aprendendo umas com as outras.

**Junte-se a nós!** E desenvolva as habilidades necessárias para o mercado de trabalho, aprimorando tanto seus conhecimentos técnicos quanto suas soft skills em um ambiente colaborativo e realista.
