# 🚀 Comercialización Digital de Productos y Servicios TI

Plataforma web moderna para la comercialización digital de productos y servicios de Tecnologías de la Información (TI).

## 📺 Ver Demo en Vivo

**🌐 Accede directamente desde tu navegador:**

👉 **https://reddragon022.github.io/Ev4_Profesionalizacion/**

La aplicación funciona completamente desde GitHub Pages sin necesidad de instalar nada. Incluye:
- ✅ 15 productos de TI organizados en 4 categorías
- ✅ 8 servicios profesionales especializados
- ✅ Estrategias de comercialización digital
- ✅ Interfaz responsive y moderna
- ✅ Filtros dinámicos por categoría

---

## 💻 Instalación Local (Opcional - Con Backend Django)

Si deseas ejecutar el proyecto localmente con el backend completo de Django:

### Requisitos
- Python 3.8+
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/RedDragon022/Ev4_Profesionalizacion.git
cd Ev4_Profesionalizacion
```

2. **Configurar el backend**
```bash
cd backend
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

3. **Crear base de datos**
```bash
python manage.py migrate
python poblar_db.py
```

4. **Iniciar servidor**
```bash
python manage.py runserver
```

5. **Abrir en navegador**
- Abre `index.html` en tu navegador
- Backend API: `http://localhost:8000/api/`

---

## 📋 Contenido

### Productos de TI (15)
- **Hardware** 🖥️: Servidores Dell PowerEdge, Cisco Catalyst, HPE ProLiant
- **Software** 📊: Microsoft 365, Salesforce, Adobe Creative Cloud, SAP
- **Cloud** ☁️: AWS EC2, Azure VM, Google Cloud, Dropbox Business
- **Seguridad** 🔒: Palo Alto, CrowdStrike, Cisco Duo, Fortinet

### Servicios (8)
1. Consultoría de Transformación Digital
2. Cloud Migration
3. Ciberseguridad y Auditoría
4. DevOps y CI/CD
5. Desarrollo de Software a Medida
6. Soporte IT 24/7
7. Business Intelligence y Analytics
8. Automatización de Procesos (RPA)

### Estrategias Digitales
- Marketing de Contenidos
- SEO y SEM
- Email Marketing Automatizado
- Redes Sociales B2B
- Webinars y Demos
- Programa de Partners

---

## 🛠️ Tecnologías

**Frontend (GitHub Pages)**
- HTML5, CSS3, JavaScript ES6+
- Diseño responsive
- Base de datos estática integrada

**Backend (Opcional)**
- Django 4.2
- Django REST Framework
- SQLite/PostgreSQL
- API RESTful completa

---

## 📁 Estructura

```
Ev4_Profesionalizacion/
├── index.html           # Página principal
├── styles.css           # Estilos
├── script.js            # Lógica JavaScript
├── productos-db.js      # Base de datos estática
├── backend/             # Backend Django (opcional)
│   ├── api/            # Modelos y API REST
│   ├── manage.py
│   └── requirements.txt
└── README.md
```

---

## 🔌 API Endpoints (Backend Local)

Si ejecutas el backend localmente:

- `GET /api/productos/` - Todos los productos
- `GET /api/productos/{id}/` - Detalle producto
- `GET /api/servicios/` - Todos los servicios
- `GET /api/categorias/` - Categorías
- `POST /api/contactos/` - Enviar contacto

---

## 👤 Autor

**RedDragon022**
- GitHub: [@RedDragon022](https://github.com/RedDragon022)
- Proyecto: [Ev4_Profesionalizacion](https://github.com/RedDragon022/Ev4_Profesionalizacion)

---

## 📄 Licencia

MIT License - Uso libre con atribución

---

⭐ **¿Te gustó el proyecto? ¡Dale una estrella en GitHub!**
