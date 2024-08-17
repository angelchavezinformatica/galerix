# Galerix

## Configuración

### Backend

#### Crear la base de datos

Para crear la base de datos, se debe ejecutar el archivo `script.sql`, para crear la base de datos y las tablas.

#### Variables de entorno

Luego se debe configurar las variables de entorno necesarias para ejercutar la aplicación.

```
# SECRET

SECRET_KEY=<secret-key>
ALGORITHM=<algorithm>

# DATABASE

DB_USER=<user>
DB_PASSWORD=<password>
DB_HOST=<host>
DB_PORT=<port>
DB_NAME=<database>
```

#### Instalar dependencias

```bash
pip install -r requirements.txt
```

#### Ejecución

```bash
fastapi dev main.py
```

### Frontend

#### Instalación de dependencias

```bash
npm install
```
