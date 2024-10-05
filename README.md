
# 006 Django 5 - Basic App 2 (Import URLconf)

Existem duas formas de criar rotas (ou URLs) amigáveis no Django. No repositório anterior [projeto nº 5](https://github.com/Django-Dev-Br/005-Django5-Basic-App), utilizamos a abordagem de importar diretamente a view do app para dentro do arquivo urls.py do projeto principal. Agora, vamos experimentar outra maneira de organizar as rotas: redirecionar para um arquivo urls.py específico do próprio app.

Essa abordagem torna o projeto mais modular e organizado, especialmente em aplicações maiores, pois cada app gerencia suas próprias URLs, facilitando a manutenção e a escalabilidade do projeto. Ao fazer isso, movemos o controle das rotas específicas para o urls.py do app, enquanto o arquivo urls.py do projeto principal apenas referencia os arquivos urls.py dos apps.

Dessa forma, o arquivo urls.py do projeto centraliza as rotas de diferentes apps, enquanto cada app se torna responsável por gerenciar suas próprias URLs.


### O que é um App Django?

Um app no Django é uma aplicação web que faz algo — um grupo de modelos, views, templates, e outras partes lógicas que tratam de um problema específico ou funcionalidade. Apps são projetados para serem reutilizáveis, plugáveis e independentes, facilitando a manutenção e a extensão de funcionalidades.

## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12 com PIP e venv**
- **o Django 5 requer Python 3.10 ou superior.**
- 
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
    git clone https://github.com/Django-Dev-Br/006-Django5-Basic-App-2.git
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

   Fazer a instalação após a ativação da virtual env fará com que a instalação seja feita nessa pasta ao invés do computador. Isso significa que o pacote Django não estará disponivel para todos os usuários do computador, mas apenas para o contexto no qual essa venv esteja ativada. Veremos sua ativação logo abaixo.

    **Instalação manualmente via gerenciador de dependências PIP**
    ```bash
    pip install django
    ```
    - use, preferencialmente, a versão 5.1. Para tanto, execute o comando:

     ```bash
    pip install  "django>=5.1,<=5.2"
    ```

    ----- **OU** -----

    **Instalação via arquivo requirements**
    ```bash
    pip install -r requirements.txt
    ```
    O arquivo requirements.txt é um arquivo de texto que contém uma lista de pacotes a ser instalado em uma venv. É uma boa prática de programação do ecossistema Python.
    

5.**Acesse a pasta do repositório**:

    ```bash
    cd 006-Django5-Basic-App-2
    ```
    
6. **Execute o servidor de desenvolvimento**:
   
    ```python
    python manage.py runserver
    ```

7. **Acesse a View no Navegador**:

   Abra o navegador e vá para o endereço [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver a mensagem:

   ```
   app up and running properly
   ```


### Como Criar um Novo App Django

Para criar um novo app em um projeto Django, use o seguinte comando:

```python
python manage.py startapp nome_do_app
```
Antes, veja como criar um projeto Django no [repositório nº 01](https://github.com/Django-Dev-Br/001-django5-basic-project/tree/main)

### Sobre Nosso Treinamento Prático-Profissional com projeto real para iniciantes e avançados em web DevOps Full-stack com Python, Django, Bootstrap e Linux.

[Django Developers Brasil - Aprenda programando enquanto programa aprendendo!](https://django.dev.br/)

Nosso treinamento oferece uma experiência prática de aprendizado de programação, adequada tanto para iniciantes quanto para desenvolvedores avançados. Você participará de um projeto real de desenvolvimento de software em um ambiente corporativo autêntico, onde pessoas com diferentes níveis de conhecimento irão colaborar, aprendendo umas com as outras.

**Junte-se a nós!** E desenvolva as habilidades necessárias para o mercado de trabalho, aprimorando tanto seus conhecimentos técnicos quanto suas soft skills em um ambiente colaborativo e realista.
