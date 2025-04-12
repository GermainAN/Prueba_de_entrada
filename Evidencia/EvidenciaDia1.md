# Prueba de Entrada
---
[Dia 2 >>](EvidenciaDia2.md)
---

## creamos la carpeta

![image.png](imagen/image.png)

## 1. creando entorno virtual de python

para luegbo instalar  `fastapi uvicorn asyncpg databases`

![image.png](imagen/image%201.png)

## 2. creamos los archivos `Dockerfile`  y `docker-compose.yml`

![image.png](imagen/image%202.png)

## 3. inicializamos el repositorio y luego creamos ramas

![image.png](imagen/image%203.png)

![image.png](imagen/image%204.png)

## 4. dockerfile

![image.png](imagen/image%205.png)

`FROM` : usamo la imagen oficial de python 3:13

`WORKDIR` : establecemos el directorio de trabjajo dentro del cotenedor /app

`COPY . .` : copia los archivos del directorio local al contenedor

`RUN` : instala las dependencias

 

## 5. docker-compose.yml

![image.png](imagen/image%206.png)

![image.png](imagen/image%207.png)

## 6. haciendo una fusion con las ramas develop y feature/dia1

![image.png](imagen/image%208.png)

## 7. git log
![imagen.png](imagen/image9.png)

---
[Dia 2 >>](EvidenciaDia2.md)
---