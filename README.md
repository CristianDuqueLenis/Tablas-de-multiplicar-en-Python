🧮 Tabla de Multiplicar en Python

Este programa en Python permite al usuario ingresar un número y genera su tabla de multiplicar del 1 al 10.
📦 Cómo clonar este repositorio

Si quieres obtener una copia local del código, puedes clonarlo desde GitHub usando:

git clone https://github.com/tu-usuario/nombre-del-repositorio.git

    🔁 Reemplaza tu-usuario y nombre-del-repositorio con tu nombre de usuario de GitHub y el nombre real del repositorio.

Luego navega al directorio clonado:

cd nombre-del-repositorio

Y ejecuta el programa:

python tabla.py

🚀 ¿Cómo funciona?

    Solicita al usuario que ingrese un número.

    Imprime la tabla de multiplicar de ese número del 1 al 10.

📋 Código fuente

# Programa crear la tabla de multiplicar de un numero dado.
numero = int(input("Ingrese el numero para su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar de {numero}")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

🖥️ Ejemplo de uso

Ingrese el numero para su tabla de multiplicar: 5
Tabla de multiplicar de 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
...
5 * 10 = 50

📎 Requisitos

    Python 3.x

✅ Cómo ejecutar

    Asegúrate de tener Python instalado.

    Guarda el archivo como tabla.py.

    Ejecuta el programa con:

python tabla.py

https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)

👤 Autor

Este repositorio fue creado por Cristian Duque.
