import os

# Antes de rodar o script:
# 1 - Crie o ambiente virtual (python -m venv venv)
# 2 - Ative o ambiente virtual ( cd venv\scripts -> Activate)
# 3 - Instale as dependências  ( pip install -r requirements.txt)
# 4 - Navegue no terminal até a pasta que contém o arquivo manage.py
# 5 - Rode este script

os.system("manage.py makemigrations")
os.system("manage.py migrate")
os.system("manage.py createsuperuser")
os.system("manage.py runserver")