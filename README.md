# Página Web de Comercialización Digital - Productos y Servicios TI

## 📋 Descripción del Proyecto

Aplicación web full-stack completa con **backend Django** y **frontend moderno** que presenta:
- **Base de datos real** con productos TI actuales (Hardware, Software, Cloud, Seguridad)
- **API REST** completa con Django REST Framework
- **Catálogo de servicios profesionales** de TI
- **Estrategias de comercialización digital** con mejores resultados comprobados
- **Panel de administración** para gestionar contenido

## 🏗️ Arquitectura del Proyecto

- **Backend**: Django 4.2 + Django REST Framework + SQLite
- **Frontend**: HTML5 + CSS3 + JavaScript (Vanilla)
- **API**: RESTful API con endpoints completos
- **Base de Datos**: SQLite (fácilmente migrable a PostgreSQL)

## 🚀 Características Principales

### 1. Productos de TI
- **Hardware**: Servidores Dell PowerEdge, Switches Cisco, HPE ProLiant
- **Software**: Microsoft 365, Salesforce, Adobe Creative Cloud, SAP S/4HANA
- **Cloud**: AWS EC2, Azure VMs, Google Cloud Platform, Dropbox Business
- **Seguridad**: Palo Alto Networks, CrowdStrike, Cisco Duo, Fortinet

### 2. Servicios Profesionales
- Consultoría de Transformación Digital
- Cloud Migration
- Ciberseguridad y Auditoría
- DevOps y CI/CD
- Desarrollo de Software a Medida
- Soporte IT 24/7
- Business Intelligence y Analytics
- Automatización de Procesos (RPA)

### 3. Estrategias de Comercialización Digital
- **Marketing de Contenidos**: ROI +400% en engagement
- **SEO y SEM**: +250% en tráfico orgánico
- **Redes Sociales**: +300% en interacciones
- **Email Marketing**: +4200% retorno promedio
- **Marketing de Influencers**: +92% en confianza
- **Marketing de Datos**: +230% en conversión

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 4.2**: Framework web de Python
- **Django REST Framework**: API REST completa
- **SQLite**: Base de datos (migrable a PostgreSQL)
- **django-cors-headers**: Manejo de CORS
- **python-decouple**: Variables de entorno

### Frontend
- **HTML5**: Estructura semántica y moderna
- **CSS3**: Diseño responsive con animaciones
- **JavaScript (Vanilla)**: Funcionalidad interactiva con Fetch API
- **Google Fonts**: Tipografía Inter

## 📁 Estructura de Archivos

```
ev4/
├── backend/                    # Backend Django
│   ├── api/                   # Aplicación API
│   │   ├── models.py         # Modelos de BD (Producto, Servicio, Categoria, Contacto)
│   │   ├── views.py          # ViewSets para la API
│   │   ├── serializers.py    # Serializers de Django REST Framework
│   │   ├── admin.py          # Configuración del panel admin
│   │   └── urls.py           # URLs de la API
│   ├── backend/               # Configuración del proyecto Django
│   │   ├── settings.py       # Configuración principal
│   │   └── urls.py           # URLs principales
│   ├── manage.py             # Comando principal de Django
│   ├── poblar_db.py          # Script para poblar base de datos inicial
│   ├── requirements.txt      # Dependencias de Python
│   └── README.md             # Documentación del backend
├── index.html                # Página principal del frontend
├── styles.css                # Estilos CSS modernos y responsive
├── script.js                 # JavaScript que consume la API
├── INSTRUCCIONES.md          # Guía paso a paso para iniciar el proyecto
└── README.md                 # Este archivo
```

## 🎨 Características de Diseño

- **Diseño Dark Mode**: Colores modernos con tema oscuro
- **Responsive**: Se adapta a móviles, tablets y escritorio
- **Animaciones**: Efectos suaves al hacer scroll
- **Gradientes**: Uso de gradientes modernos
- **Iconos Emoji**: Visuales atractivos sin dependencias externas

## 🔧 Funcionalidades Interactivas

1. **Filtros de Productos**: Filtra por Hardware, Software, Cloud o Seguridad
2. **Carga Dinámica**: Productos y servicios se cargan desde la base de datos
3. **Menú Responsive**: Hamburger menu para dispositivos móviles
4. **Smooth Scroll**: Navegación suave entre secciones
5. **Formulario de Contacto**: Validación y manejo de envío
6. **Animaciones al Scroll**: Aparición progresiva de elementos
7. **Header Dinámico**: Cambia de apariencia al hacer scroll

## 📊 Estadísticas Incluidas

- 87% de compradores investigan online antes de comprar
- $4.9T mercado global de e-commerce en 2024
- 73% de empresas usan IA para marketing
- 2.64B usuarios activos en redes sociales

## 🚀 Inicio Rápido

### Lee las instrucciones completas en: **[INSTRUCCIONES.md](INSTRUCCIONES.md)**

### Resumen:

1. **Configurar Backend**:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python poblar_db.py
python manage.py runserver
```

2. **Abrir Frontend**:
   - Abre `index.html` en tu navegador o con Live Server de VS Code

3. **Acceder al Admin**:
   - http://localhost:8000/admin

## 🌐 Uso de la Aplicación

1. **Panel Admin**: Gestiona productos, servicios y mensajes en http://localhost:8000/admin
2. **API REST**: Accede a los datos en http://localhost:8000/api/
3. **Frontend**: Navega por el sitio web con datos en tiempo real
4. **Filtrar productos**: Usa los botones de filtro por categoría
5. **Ver detalles**: Click en "Ver Detalles" para información completa
6. **Contacto**: El formulario guarda directamente en la base de datos

## 💡 Personalización

### Agregar más productos
**Opción 1: Panel de Administración (Recomendado)**
1. Ve a http://localhost:8000/admin
2. Click en "Productos" → "Agregar producto"
3. Llena el formulario y guarda

**Opción 2: Directamente en la base de datos**
```python
# En el shell de Django (python manage.py shell)
from api.models import Producto, Categoria, CaracteristicaProducto

categoria = Categoria.objects.get(nombre='hardware')
producto = Producto.objects.create(
    nombre="Nuevo Producto",
    categoria=categoria,
    icon="🆕",
    descripcion="Descripción del producto",
    precio="$999",
    precio_numerico=999.00,
    stock=10
)
CaracteristicaProducto.objects.create(
    producto=producto,
    descripcion="Característica 1"
)
```

### Agregar más servicios
1. Ve a http://localhost:8000/admin
2. Click en "Servicios" → "Agregar servicio"
3. Llena el formulario y guarda

### Cambiar colores del frontend
Edita las variables CSS en `styles.css`:

```css
:root {
    --primary-color: #0066ff;
    --secondary-color: #00d4ff;
    /* ... más variables */
}
```

### Cambiar URL de la API
Edita en `script.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api';
```

## 📱 Responsividad

La página está optimizada para:
- **Móviles**: < 768px
- **Tablets**: 768px - 968px
- **Escritorio**: > 968px

## ⚡ Rendimiento

- Sin dependencias externas pesadas
- Imágenes optimizadas (usando emojis)
- CSS y JS optimizados
- Carga rápida y eficiente

## 🎯 Casos de Uso

Esta página es ideal para:
- Empresas de TI que venden productos y servicios
- Consultoras de tecnología
- Distribuidores de hardware y software
- Proyectos educativos sobre comercialización digital
- Portfolios de servicios tecnológicos

## 📞 Información de Contacto

La página incluye una sección de contacto con:
- Formulario de contacto funcional
- Email: info@tidigital.com
- Teléfono: +52 (55) 1234-5678
- Ubicación: Ciudad de México, México

## 📡 API REST Endpoints

### Productos
- `GET /api/productos/` - Lista todos los productos
- `POST /api/productos/` - Crear producto
- `GET /api/productos/{id}/` - Detalle de producto
- `PUT/PATCH /api/productos/{id}/` - Actualizar producto
- `DELETE /api/productos/{id}/` - Eliminar producto
- `GET /api/productos/destacados/` - Productos destacados
- `GET /api/productos/?categoria__nombre=hardware` - Filtrar por categoría

### Servicios
- `GET /api/servicios/` - Lista todos los servicios
- `POST /api/servicios/` - Crear servicio
- `GET /api/servicios/{id}/` - Detalle de servicio
- `GET /api/servicios/destacados/` - Servicios destacados

### Contactos
- `GET /api/contactos/` - Lista contactos
- `POST /api/contactos/` - Crear contacto (desde formulario)

### Categorías
- `GET /api/categorias/` - Lista categorías

Ver documentación completa en: [backend/README.md](backend/README.md)

## 🔄 Mejoras Futuras Sugeridas

- [ ] Sistema de carrito de compras
- [ ] Pasarela de pagos (Stripe, PayPal)
- [ ] Autenticación de usuarios (JWT)
- [ ] Blog de contenidos con Django
- [ ] Sistema de reseñas y ratings
- [ ] Chat en vivo
- [ ] Notificaciones por email
- [ ] Panel de analytics
- [ ] Exportación de reportes
- [ ] Búsqueda avanzada con Elasticsearch

## 📄 Licencia

Este proyecto es para uso educativo y comercial.

## 👨‍💻 Autor

Creado para el proyecto de Profesionalización - 6to Semestre

---

**¡Disfruta explorando las mejores estrategias de comercialización digital para productos TI!** 🚀
