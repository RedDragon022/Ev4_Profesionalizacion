# 🚀 Guía Rápida de Inicio

## Paso 1: Instalar y Configurar Backend Django

### 1.1 Abrir terminal en la carpeta del proyecto

```bash
cd "C:\Users\angel\OneDrive\Escritorio\Uni\6to semestre\Profesionalizacion\ev4"
```

### 1.2 Navegar a la carpeta backend y crear entorno virtual

```bash
cd backend
python -m venv venv
```

### 1.3 Activar el entorno virtual

**En Windows (PowerShell):**
```bash
venv\Scripts\activate
```

**Si hay error de permisos en PowerShell, usar:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

**O usar CMD en lugar de PowerShell:**
```bash
venv\Scripts\activate.bat
```

### 1.4 Instalar dependencias

```bash
pip install -r requirements.txt
```

### 1.5 Crear base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 1.6 Crear usuario administrador

```bash
python manage.py createsuperuser
```

Te pedirá:
- Username: (elige uno, ej: admin)
- Email: (tu email)
- Password: (elige una contraseña)

### 1.7 Poblar base de datos con productos y servicios

```bash
python poblar_db.py
```

### 1.8 Iniciar servidor Django

```bash
python manage.py runserver
```

✅ El backend estará disponible en: **http://localhost:8000**

**NO CIERRES ESTA TERMINAL** - El servidor debe seguir ejecutándose

---

## Paso 2: Abrir Frontend

### 2.1 Abrir nueva terminal (PowerShell o CMD)

### 2.2 Navegar al directorio raíz del proyecto

```bash
cd "C:\Users\angel\OneDrive\Escritorio\Uni\6to semestre\Profesionalizacion\ev4"
```

### 2.3 Abrir index.html con Live Server de VS Code

**Opción 1: Desde VS Code**
1. Abre `index.html` en VS Code
2. Click derecho → "Open with Live Server"

**Opción 2: Abrir directamente en navegador**
1. Abre el archivo `index.html` directamente en tu navegador
2. URL será algo como: `file:///C:/Users/angel/OneDrive/Escritorio/Uni/6to%20semestre/Profesionalizacion/ev4/index.html`

---

## 🎯 Verificación

### Verifica que todo funciona:

1. **Backend Django**: http://localhost:8000/admin
   - Inicia sesión con tu superusuario
   - Verás el panel de administración

2. **API REST**: http://localhost:8000/api/
   - Deberías ver la lista de endpoints disponibles

3. **Productos**: http://localhost:8000/api/productos/
   - Deberías ver JSON con los productos

4. **Frontend**: Abre `index.html` en navegador
   - Los productos y servicios deberían cargarse automáticamente desde la API

---

## 📊 Panel de Administración Django

Accede a: **http://localhost:8000/admin**

Desde aquí puedes:
- ✏️ Agregar/editar/eliminar productos
- ✏️ Agregar/editar/eliminar servicios
- 📧 Ver mensajes de contacto recibidos
- 📂 Gestionar categorías

---

## 🔧 Comandos Útiles

### Ver todos los productos en la API:
```bash
# En tu navegador:
http://localhost:8000/api/productos/
```

### Ver productos por categoría:
```bash
http://localhost:8000/api/productos/?categoria__nombre=hardware
http://localhost:8000/api/productos/?categoria__nombre=software
http://localhost:8000/api/productos/?categoria__nombre=cloud
http://localhost:8000/api/productos/?categoria__nombre=seguridad
```

### Ver servicios:
```bash
http://localhost:8000/api/servicios/
```

### Detener el servidor Django:
Presiona `Ctrl + C` en la terminal donde corre el servidor

---

## ❗ Solución de Problemas

### Problema: "Error al cargar productos" en el frontend

**Solución:**
1. Verifica que el servidor Django esté ejecutándose en http://localhost:8000
2. Abre la consola del navegador (F12) para ver errores
3. Verifica que CORS esté configurado correctamente

### Problema: Error de permisos al activar venv en PowerShell

**Solución:**
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: "Module not found" al instalar dependencias

**Solución:**
```bash
# Asegúrate de estar en el directorio backend
cd backend
# Y que el entorno virtual esté activado
venv\Scripts\activate
# Luego instala de nuevo
pip install -r requirements.txt
```

### Problema: No aparecen datos en el frontend

**Solución:**
1. Verifica que ejecutaste `python poblar_db.py`
2. Verifica en el admin: http://localhost:8000/admin
3. Revisa la consola del navegador (F12) para ver errores de CORS

---

## 📁 Estructura del Proyecto

```
ev4/
├── backend/                    # Backend Django
│   ├── api/                   # Aplicación API
│   │   ├── models.py         # Modelos de BD
│   │   ├── views.py          # ViewSets
│   │   ├── serializers.py    # Serializers
│   │   ├── admin.py          # Configuración admin
│   │   └── urls.py           # URLs de la API
│   ├── backend/               # Configuración Django
│   │   ├── settings.py       # Configuración principal
│   │   └── urls.py           # URLs principales
│   ├── manage.py             # Comando Django
│   ├── poblar_db.py          # Script para datos iniciales
│   ├── requirements.txt      # Dependencias Python
│   └── README.md             # Documentación backend
├── index.html                # Frontend principal
├── styles.css                # Estilos CSS
├── script.js                 # JavaScript (conecta con API)
├── productos-db.js           # (Ya no se usa - datos en Django)
└── README.md                 # Documentación general
```

---

## 🎓 Para tu Proyecto Universitario

### Funcionalidades Implementadas:

✅ **Base de datos real** con Django ORM
✅ **API REST completa** con Django REST Framework
✅ **CRUD completo** (Crear, Leer, Actualizar, Eliminar)
✅ **15 productos de TI actuales** en 4 categorías
✅ **8 servicios profesionales** de TI
✅ **Estrategias de comercialización digital** documentadas
✅ **Panel de administración** Django
✅ **Frontend responsive** conectado a la API
✅ **Formulario de contacto** que guarda en BD

### Para Demostrar:

1. **Base de Datos**: Muestra el panel admin con productos
2. **API REST**: Muestra los endpoints en el navegador
3. **Frontend Dinámico**: Muestra cómo se cargan los datos
4. **Filtros**: Demuestra el filtrado por categoría
5. **Formulario**: Envía un contacto y muéstralo en el admin

---

## 🚀 ¡Listo para Usar!

Tu proyecto ahora tiene:
- ✅ Backend profesional con Django
- ✅ Base de datos SQLite (o puedes cambiar a PostgreSQL)
- ✅ API REST completamente funcional
- ✅ Frontend moderno y responsive
- ✅ Datos reales de productos y servicios TI
- ✅ Estrategias de comercialización digital documentadas

**¡Todo funcionando con soporte de base de datos completo!**
