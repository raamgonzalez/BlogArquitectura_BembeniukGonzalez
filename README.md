# Blog de Arquitectura. Autores: Bembeniuk_Gonzalez #

## Descarga ##
Desde una consola o el bash de git usar el siguiente comando:
- git clone https://github.com/raamgonzalez/Entrega1_BembeniukGonzalez.git

## Instalación ##
1. pip install -r requirements.txt
2. python manage.py migrate
3. python manage.py runserver

## Contenido del blog / explicación del proyecto ##
1. Se crea una página de inicio /index, en la cual se da una bienvenda al sitio
2. Se crea una página de "Nosotros" en la cual describimos brevemente el proyecto y nuestros intereses
3. Se crea una página de contacto
5. Se pide registro y logueo para poder hacer uso de los formularios
6. Se proponen 2 clases en "models": "Obras de Arquitectura" y "Arquitectos", siendo esta ultima una categría de la primera
7. Cada modelo cuenta con un formulario que permite agregar contenido
8. Se incorpora un boton "search" para poder buscar en la base de datos

## Funcionalidades ##
### Contenidos desarollados en la preentrega ###
- Se crea una template "base.html" de la cual se heredan caracteristicas
- Las 3 clases se crean en models.py
- Los formularios se crean en forms.py
- Se usa el comando "git push -u origin main" para mandar los archivos al repository de github

### Contenidos desarollados para la entrega final ###
8º COMMIT
- Se genera enlace Arquitectos con Obras mediante categoría.
- Se agrega campo de descripción en Obra de Arquitectura para que se vea solo en ‘detail’
- Se agrega método __str__ para que se lea el nombre de la categoria
- Se agrega template de "Nosotros" + boton en base

9º COMMIT
- Se reordena proyecto:
- Se aplica CRUD: Listview, DetailView, CreateView, UpdateView, DeleteView

10º COMMIT
- Se agregua template delete_obra y delete_arqui
- Se corrige botón de Search para poder realizar búsqueda
- Se incorpora la posibilidad de eliminar obra o arquitecto
- Se corrigen los forms
- Se incorpora el botón delete en views.py
- se aplica reverse a obra y arqui
- Se modifican textos en html

11º COMMIT
- Se agrega login_view
- Se agrega logout_view
- Se agrega register_view
- Se crea template de login y register en carpeta auth
- Se modifica el base para que si estás logueado no salga el boton login
- Se crean restricciones (mixins) a la hora de cargar un Arquitecto o Obra (es necesario estar registrado)
- Se crean restricciones (decorador) a la hora de entrar a contacto
- Se crea template de Contacto

12º COMMIT
- Se agrega app users
- Se agrega en setting MEDIA_URL y MEDIA_ROOT
- Se genera class de User_profile
- Se agrega descripción a arquitectos
- Se instala Pillow
- Se actualiza requirements.txt
- Se agregan imágenes a arquitectos y obras
- Se ordenan los html de obras y arqui para que aparezcan mejor en la pag.
- Se crean algunas obras y arquitectos para probar + 2 usuarios. Todo completo

13°COMMIT
- Se creo la app “index” para que los textos de contenido del sitio sean editados por admin. 

14º COMMIT
- Se agrega UpdateProfile
- Se agrega DetailProfile
- Se agregan templates correspondientes
- Se actualizan html y se mejora la calidad de visualización del sitio



