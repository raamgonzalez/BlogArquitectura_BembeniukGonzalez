# blogArquitectura_BembeniukGonzalez
## Descarga ##
Desde una consola o el bash de git usar el siguiente comando
- git clone https://github.com/raamgonzalez/Entrega1_BembeniukGonzalez.git
## Instalación ##
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

## Contenido del blog / explicación del proyecto ##
1. Se crea un página de inicio /index, en la cual se describe brevemente el contenido
2. Se proponen 3 clases en "models": "obras de Arquitectura", "Instituciones" y "Bibliografía. Cada clase es independiente de las otras.  
3. Cada modelo cuenta con un formulario que permite agregar contenido
4. Se incorpora un boton "search" para poder buscar en la base de datos

## Funcionalidades ##
- Se crea una template "base.html" de la cual se heredan caracteristicas
- Las 3 clases se crean en models.py
- Los formularios se crean en forms.py
