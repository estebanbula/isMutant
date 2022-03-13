# Examen Mercadolibre
Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens. Te ha contratado a ti para que desarrolles un proyecto que detecte 
si un humano es mutante basándose en su secuencia de ADN. Para eso te ha pedido crear un programa con un método o función con la siguiente firma: 
boolean isMutant(String[] dna);
En donde recibirás como parámetro un array de Strings que representan cada fila de una tabla de (NxN) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.

![image](https://user-images.githubusercontent.com/36938874/158068762-c2ee18b6-d511-487f-81d8-71070bb243da.png)

Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras
iguales​, de forma oblicua, horizontal o vertical.

sequencias = ['AAAA', 'TTTT', 'CCCC', 'GGGG']

## Desafíos:
### Nivel 1:
Programa (en cualquier lenguaje de programación) que cumpla con el método pedido por
Magneto.
### Nivel 2:
Crear una API REST, hostear esa API en un cloud computing libre (Google App Engine,
Amazon AWS, etc), crear el servicio “/mutant/” en donde se pueda detectar si un humano es
mutante enviando la secuencia de ADN mediante un HTTP POST con un Json el cual tenga el
siguiente formato:
POST → /mutant/
{
“dna”:["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
}
En caso de verificar un mutante, debería devolver un HTTP 200-OK, en caso contrario un
403-Forbidden
### Nivel 3:
Anexar una base de datos, la cual guarde los ADN’s verificados con la API.
Solo 1 registro por ADN.
Exponer un servicio extra “/stats” que devuelva un Json con las estadísticas de las
verificaciones de ADN: {“count_mutant_dna”: 40, “count_human_dna”: 100: “ratio”: 0.4}
Tener en cuenta que la API puede recibir fluctuaciones agresivas de tráfico (Entre 100 y 1
millón de peticiones por segundo).
Test-Automáticos, Code coverage > 80%.

## Solución:
Se implementa una solución recorriendo la matriz de ADN cada 4 caracteres, utilizando variables de
control para la posición de la cadena de ADN dentro del array (variable i) y para la posición del carácter
dentro del string (variable j), cada una de estas variables iterando dentro del rango de objetos incluidos
en el dna (len(dna)).

## Detalles de la implementación:
* Lenguaje de programación: Python 3.7
* Framework backend: Django
* Api Framework: Django Rest Framework
* Base de datos: MySQL (Cloud SQL)
* Cloud Computing: Google App Engine

## URL App Engine:
* https://is-mutant-mercadolibre.uc.r.appspot.com/

# Pasos para reproducir:

## Nivel 1

### Requisitos:
* Python 3.7
* virtualenv

## Para ejecutar Localmente:
* Código fuente del algoritmo: mutants/ismutant/views.py

Se recomienda clonar el repositorio y utilizar un cliente Postman o Insomnia

Estando dentro del directorio isMutant ejecutar la siguente línea en la terminal la creación del entorno virtual:

* En Windows: `py -m venv venv`
* En Mac o Linux: `python -m venv venv`

Para activar el entorno virtual de Python:

* En Windows
`.\venv\Scripts\activate`
* En Mac o Linux
`source venv/bin/activate`

Para instalar las dependencias del proyecto:

`pip install -r requirements.txt`

Con lo anterior ejecutado correctamente, desde la línea de comandos nos movemos al directorio `mutants`, dentro de isMutant y ejecutamos la siguente línea para ejecutar el servidor en local y en el puerto 8080

* En Windows: `py manage.py manage.py runserver 8080`
* En Mac y Linux: `python manage.py runserver 8080`

Ahora se puede realizar la petición:

> POST → http://localhost:8080/mutant/
> 
> Body:
> 
> {
> "dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
> }

Response:

> HttpStatus 200 OK

Ejemplo caso no mutante:

> POST → http://localhost:8080/mutant/
> 
> Body:
> 
> {
> "dna":["GTGCGA","CAGTGC","TTATGT","AGAAAG","CTCCTA","TCACTG"]
> }

Reponse: 

> HttpStatus 403 FORBIDDEN

## Nivel 2

* Api creada y Hosteada en Google App Engine: `https://is-mutant-mercadolibre.uc.r.appspot.com/mutant/`

Caso mutante:

> POST → https://is-mutant-mercadolibre.uc.r.appspot.com/mutant/
> 
> Body:
> 
> {
> "dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
> }

Response:

> HttpStatus 200 OK

Ejemplo caso no mutante:

> POST → https://is-mutant-mercadolibre.uc.r.appspot.com/mutant/
> 
> Body:
> 
> {
> "dna":["GTGCGA","CAGTGC","TTATGT","AGAAAG","CTCCTA","TCACTG"]
> }

Reponse: 

> HttpStatus 403 FORBIDDEN
