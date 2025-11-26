# Backend Django - Productos y Servicios TI

Backend API REST desarrollado con Django y Django REST Framework para gestionar productos y servicios de TI.

## 🚀 Instalación y Configuración

### 1. Crear entorno virtual

```bash
# Navegar a la carpeta backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
# Copiar el archivo de ejemplo
copy .env.example .env

# Editar .env con tus configuraciones
```

### 4. Crear base de datos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

### 5. Crear superusuario (admin)

```bash
python manage.py createsuperuser
```

### 6. Poblar base de datos con datos iniciales

```bash
python poblar_db.py
```

### 7. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

## 📚 Endpoints de la API

### Categorías
- `GET /api/categorias/` - Lista todas las categorías
- `GET /api/categorias/{id}/` - Detalle de una categoría

### Productos
- `GET /api/productos/` - Lista todos los productos
- `POST /api/productos/` - Crear nuevo producto
- `GET /api/productos/{id}/` - Detalle de un producto
- `PUT /api/productos/{id}/` - Actualizar producto completo
- `PATCH /api/productos/{id}/` - Actualizar producto parcial
- `DELETE /api/productos/{id}/` - Eliminar producto
- `GET /api/productos/destacados/` - Productos destacados
- `GET /api/productos/por_categoria/?categoria=hardware` - Filtrar por categoría

### Servicios
- `GET /api/servicios/` - Lista todos los servicios
- `POST /api/servicios/` - Crear nuevo servicio
- `GET /api/servicios/{id}/` - Detalle de un servicio
- `PUT /api/servicios/{id}/` - Actualizar servicio completo
- `PATCH /api/servicios/{id}/` - Actualizar servicio parcial
- `DELETE /api/servicios/{id}/` - Eliminar servicio
- `GET /api/servicios/destacados/` - Servicios destacados

### Contactos
- `GET /api/contactos/` - Lista todos los contactos
- `POST /api/contactos/` - Crear nuevo contacto
- `GET /api/contactos/{id}/` - Detalle de un contacto
- `PATCH /api/contactos/{id}/marcar_leido/` - Marcar como leído

## 🔍 Filtros y Búsqueda

### Productos
```bash
# Buscar por nombre o descripción
GET /api/productos/?search=servidor

# Filtrar por categoría
GET /api/productos/?categoria=1

# Filtrar destacados
GET /api/productos/?destacado=true

# Ordenar por precio
GET /api/productos/?ordering=precio_numerico

# Ordenar descendente
GET /api/productos/?ordering=-precio_numerico

# Combinar filtros
GET /api/productos/?categoria=1&destacado=true&ordering=-precio_numerico
```

### Servicios
```bash
# Buscar
GET /api/servicios/?search=cloud

# Ordenar
GET /api/servicios/?ordering=precio_numerico
```

## 🎨 Panel de Administración

Accede al panel admin en: `http://localhost:8000/admin/`

Funcionalidades:
- Gestión completa de productos con características inline
- Gestión de servicios
- Ver y gestionar mensajes de contacto
- Filtros y búsqueda avanzada
- Exportación de datos

## 📊 Modelos de Base de Datos

### Categoria
- nombre (hardware, software, cloud, seguridad)
- descripcion
- icon

### Producto
- nombre
- categoria (FK)
- icon
- descripcion
- precio (string para display)
- precio_numerico (decimal para ordenamiento)
- fabricante
- modelo
- destacado
- stock
- activo
- features (relación inversa con CaracteristicaProducto)

### Servicio
- nombre
- icon
- descripcion
- precio
- precio_numerico
- duracion_estimada
- nivel_complejidad
- destacado
- activo

### Contacto
- nombre
- email
- telefono
- mensaje
- producto_interes (FK opcional)
- servicio_interes (FK opcional)
- leido
- respondido

## 🔒 CORS

El backend está configurado para aceptar requests desde:
- `http://localhost:3000`
- `http://localhost:5500` (Live Server VS Code)
- Todos los orígenes en modo desarrollo

## 🗄️ Base de Datos

Por defecto usa SQLite (`db.sqlite3`).

Para usar PostgreSQL:
1. Instalar psycopg2: `pip install psycopg2-binary`
2. Configurar en `.env`:
```
DB_NAME=ti_productos
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
```
3. Descomentar la configuración de PostgreSQL en `settings.py`

## 📝 Ejemplos de Uso

### Crear un producto desde la API

```json
POST /api/productos/
{
  "nombre": "Nuevo Producto",
  "categoria": 1,
  "icon": "🆕",
  "descripcion": "Descripción del producto",
  "precio": "$999",
  "precio_numerico": 999.00,
  "fabricante": "Fabricante X",
  "modelo": "Modelo Y",
  "destacado": true,
  "stock": 50,
  "features": [
    "Característica 1",
    "Característica 2",
    "Característica 3"
  ]
}
```

### Enviar formulario de contacto

```json
POST /api/contactos/
{
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "telefono": "+52 55 1234 5678",
  "mensaje": "Me interesa el servicio de Cloud Migration",
  "servicio_interes": 2
}
```

## 🛠️ Comandos Útiles

```bash
# Ver migraciones pendientes
python manage.py showmigrations

# Crear datos de prueba
python manage.py shell
>>> from api.models import *
>>> # crear objetos aquí

# Limpiar base de datos
python manage.py flush

# Abrir shell de Django
python manage.py shell

# Ejecutar tests
python manage.py test
```

## 📦 Dependencias Principales

- Django 4.2
- Django REST Framework 3.14
- django-cors-headers 4.3
- python-decouple 3.8
- django-filter (incluido en DRF)

## 🔐 Seguridad

- SECRET_KEY en variable de entorno
- DEBUG=False en producción
- CORS configurado apropiadamente
- Validación de datos con serializers
- CSRF protection habilitado

## 🚀 Despliegue en Producción

1. Configurar variables de entorno
2. Establecer `DEBUG=False`
3. Configurar `ALLOWED_HOSTS`
4. Usar base de datos PostgreSQL
5. Configurar archivos estáticos: `python manage.py collectstatic`
6. Usar servidor WSGI (Gunicorn)
7. Configurar HTTPS
8. Restringir CORS a dominios específicos

## 📄 Licencia

Este proyecto es para uso educativo y comercial.
