# Subir una carpera o carpetas a Github

ir a Github, e iniciar sesión

http://github.com/

Ahora vamos a Visual Studio Code, en la parte inferior izquierda, donde se ve un logo de perfil, verificar si una persona dejó la inicio abiera, le damos click en la cuenta de la persona y presionar sign out

Invocar la termina, en la parte superior en terminal --> New Terminal 

Introducir lo siguientes comandos en la terminal 

Introducir el nombre de Usuario GitHub, en la parte superior derecha de GitHub, darle en profile, el que esta en la parte superior izquierda
git config --global user.name nombreUsuario

Introducir el correo con el que se regitraron el GitHub
git config --global user.email correoUsuario

Visual Studio Code como editor de GitHub

git config --global core.edutor "code --wair"

# Para subir a GitHub

Parte lateral izquierda, generalmente click debajo de la lupa, en la opción source control o CTRL+SHIFT+G

Le damos al botón inicializar repositorio, sino aparece esa opción borrar el archivo oculto .git de la o las carpetas contenedoras

COLOCAR MENSAJE OBLIGATORIO de que fue lo que se hizo y darle en commit

Si aparece una ventana de que no aparece los archivos en stagged, si queremos pasarlos directamente le presionamos que si

Nos arrojará a una ventana independiente para iniciar sesión en GitHub, colocamos correo y contraseña y se devuelve a vsc

Luego nos pide si queremos un repositorio público o privado, le damos en público

y luego los archivos estarán en GitHub en la parte superior derecha, en la parte de logo, darle en repositorios 