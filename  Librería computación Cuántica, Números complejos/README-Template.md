# Libreria de números complejos

El siguiente proyecto tiene como objetivo proporcionar una herramienta para realizar operaciones básicas con números complejos, así como en espacios vectoriales complejos

### Instalación y requisitos

Para probar el funcionamiento del programa desarrollado, se requiere descargar los archivos "Operations.py" y su "test.py". Además, es necesario contar con un entorno de desarrollo como PyCharm o Visual Studio para visualizar y ejecutar el proyecto.

## Ejecución de las pruebas

Cada operación ofrecida en esta calculadora básica de números complejos tiene definidas dos pruebas para verificar su funcionalidad inicialmente. Utilizamos la librería unittest para comparar los valores que deberíamos obtener, lo que nos permite ejecutar las pruebas fácilmente y detectar errores.


### ¿ Por que estas pruebas?

A lo largo de las pruebas, se implementaron diversos ejemplos utilizando diferentes números complejos para verificar el correcto funcionamiento de la calculadora. Por ejemplo, en la suma, se utilizó la operación (-1 + 2i) + (1 - 2i) para evaluar el funcionamiento general con distintos tipos de números.

Para la resta, se empleó la operación (-1-2i) - (3+4i) para validar que se mantuviera el signo negativo durante el cálculo, asegurando la separación adecuada de las partes real e imaginaria para obtener el resultado correcto (5 - 10i).

En cuanto a la división, se seleccionaron pruebas que resultarían en números complejos con partes decimal tanto en la parte real como en la imaginaria, con el propósito de detectar posibles problemas con estos valores.

Para la operación de módulo, se utilizó el número complejo (2+2i) para verificar la precisión del cálculo con números decimales.

En el caso del conjugado, se seleccionaron números comunes para asegurar que el cambio de signo se realizara correctamente.

El resto de las operaciones fueron probadas con casos generales para verificar su funcionamiento adecuado.



## Authors

* **Esteban Aguilera Contreras** - 



