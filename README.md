# desafio-sentencias-condicionales
Este repositorio contiene dos actividades desarrolladas en Python: el cálculo del Índice de Masa Corporal (IMC) y un juego de Cachipún (Piedra, Papel, Tijera) contra la computadora. Estas actividades están diseñadas para mejorar la comprensión y aplicación de conceptos de programación.

Contenido

Actividad 1 - IMC
Actividad 2 - Cachipún
Instrucciones de Instalación
Uso
Contribuciones
Licencia
Actividad 1 - IMC

El Índice de Masa Corporal (IMC) es una medida utilizada para determinar el estado nutricional de una persona, basada en su peso y altura. El IMC se calcula de la siguiente manera:

I
M
C
=
W
H
2
IMC= 
H 
2
 
W
​	
 

Donde:

W
W es el peso de la persona en kilogramos.
H
H es la altura de la persona en metros.
La Organización Mundial de la Salud (OMS) clasifica los valores del IMC en varias categorías:

IMC	Clasificación
< 18.5	Bajo Peso
18.5 - 24.9	Adecuado
25 - 29.9	Sobrepeso
30 - 34.9	Obesidad Grado I
35 - 39.9	Obesidad Grado II
> 40	Obesidad Grado III
Ejecución del Programa
Para ejecutar el programa de cálculo del IMC, utilice el siguiente comando en la terminal:

bash
Copiar código
python imc.py
Actividad 2 - Cachipún

Cachipún, también conocido como Piedra, Papel, Tijera, es un juego simple donde dos jugadores eligen uno de los tres elementos. Las reglas del juego son:

Piedra vence a Tijera.
Tijera vence a Papel.
Papel vence a Piedra.
Este programa permite jugar Cachipún contra la computadora.

Ejecución del Programa
Para ejecutar el programa de Cachipún, utilice el siguiente comando en la terminal:

bash
Copiar código
python cachipun.py
Instrucciones de Instalación

Clonar el repositorio:
bash
Copiar código
git clone https://github.com/usuario/actividades-programacion.git
Navegar al directorio del proyecto:
bash
Copiar código
cd actividades-programacion
(Opcional) Crear un entorno virtual:
bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows usar `venv\Scripts\activate`
Instalar las dependencias requeridas:
bash
Copiar código
pip install -r requirements.txt
Uso

Cálculo del IMC
Ejecute el programa imc.py.
Ingrese su peso en kilogramos cuando se le solicite.
Ingrese su altura en metros cuando se le solicite.
El programa calculará y mostrará su IMC junto con la clasificación según la OMS.
Jugar Cachipún
Ejecute el programa cachipun.py.
Elija una opción (Piedra, Papel, Tijera) cuando se le solicite.
El programa mostrará la elección de la computadora y el resultado del juego.
Contribuciones

Las contribuciones son bienvenidas. Por favor, siga los siguientes pasos:

Haga un fork del repositorio.
Cree una nueva rama (git checkout -b feature/nueva-caracteristica).
Realice sus cambios y haga commits (git commit -m 'Añadir nueva característica').
Haga push a la rama (git push origin feature/nueva-caracteristica).
Abra un Pull Request.
Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más detalles.