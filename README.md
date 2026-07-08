# Sistema de Alquiler de Bicicletas

Trabajo Final Integrador - Laboratorio de Python
Escenario 11: Sistema de alquiler de bicicletas

## Que hace el sistema

El programa permite gestionar el alquiler de bicicletas dentro de un
parque o ciudad. Con el se puede:

- Registrar, listar y modificar clientes.
- Registrar bicicletas y controlar cuales estan disponibles.
- Iniciar un alquiler (la bicicleta queda ocupada).
- Finalizar un alquiler: calcula el tiempo de uso y el importe a cobrar.
- Ver estadisticas de utilizacion (recaudacion total, tiempo total de
  uso, bicicleta mas alquilada y cliente con mas alquileres).

Los datos se guardan en archivos JSON dentro de la carpeta `datos/`,
asi que no se pierden al cerrar el programa.

## Como se calcula el importe

El importe se cobra por hora, segun la tarifa de cada bicicleta.
Si el cliente usa una fraccion de hora, se le cobra la hora completa.
El minimo que se cobra es 1 hora.

Ejemplo: una bicicleta de $1500 por hora usada durante 90 minutos
cobra 2 horas, es decir $3000.

## Como ejecutar el programa

Parado en la carpeta del proyecto, ejecutar:

    python main.py

No hace falta instalar nada: el programa usa unicamente la libreria
estandar de Python.

## Archivos del proyecto

- **main.py**: programa principal. Carga los datos y muestra el menu.
- **cliente.py**: clase Cliente (dni, nombre, apellido, telefono).
- **bicicleta.py**: clase Bicicleta (codigo, tipo, tarifa, disponible).
- **alquiler.py**: clase Alquiler (numero, cliente, bicicleta, fechas,
  importe, si esta finalizado).
- **utilidades.py**: funciones simples para pedir datos por teclado.
- **persistencia.py**: guarda y carga los datos en archivos JSON.
- **gestion_clientes.py**: registrar, listar, buscar y modificar clientes.
- **gestion_bicicletas.py**: registrar, listar y ver bicicletas disponibles.
- **gestion_alquileres.py**: iniciar y finalizar alquileres, calcular el
  tiempo de uso y el importe, y listar alquileres.
- **estadisticas.py**: calcula las estadisticas de utilizacion.
- **datos/**: carpeta donde se guardan los archivos JSON
  (clientes.json, bicicletas.json, alquileres.json). Se crean solos la
  primera vez que se guarda un dato.
