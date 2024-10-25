# Usa la imagen oficial de Python
FROM python:3.11

# Instala las dependencias del sistema necesarias para compilar psycopg2
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean

# Configura el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto 8000 para Django
EXPOSE 8000

# Ejecuta el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
