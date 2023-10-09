# Python
## Usando Linux

### Criar ambiente 
python3 -m venv venv

### Ativar ambiente
source venv/bin/activate

### Instalar biblioteca Django
pip install django

### Instalar biblioteca para trabalhar com imagens

pip install pillow

### Instalar biblioteca para gerar PDF de HTML

pip install weasyprint

### Criar projeto
django-admin startproject <nome_do_projeto> .

### Criar aplicativos
python3 manage.py startapp <nome_do_app>

### Criar migrações
python3 manage.py makemigrations

### Executar migrações
python3 manage.py migrate

### Criar Super Usuário
python3 manage.py createsuperuser

### Rodar servidor
python3 manage.py runserver