"""
Script para poblar la base de datos con datos iniciales
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Categoria, Producto, CaracteristicaProducto, Servicio


def poblar_base_datos():
    print("🚀 Iniciando población de base de datos...")
    
    # Crear categorías
    print("\n📁 Creando categorías...")
    categorias = {
        'hardware': Categoria.objects.get_or_create(
            nombre='hardware',
            defaults={'descripcion': 'Equipos y dispositivos de hardware', 'icon': '🖥️'}
        )[0],
        'software': Categoria.objects.get_or_create(
            nombre='software',
            defaults={'descripcion': 'Aplicaciones y sistemas de software', 'icon': '💻'}
        )[0],
        'cloud': Categoria.objects.get_or_create(
            nombre='cloud',
            defaults={'descripcion': 'Servicios en la nube', 'icon': '☁️'}
        )[0],
        'seguridad': Categoria.objects.get_or_create(
            nombre='seguridad',
            defaults={'descripcion': 'Soluciones de ciberseguridad', 'icon': '🔒'}
        )[0],
    }
    print(f"✅ {len(categorias)} categorías creadas")
    
    # Crear productos
    print("\n📦 Creando productos...")
    
    productos_data = [
        # Hardware
        {
            'nombre': 'Dell PowerEdge R750',
            'categoria': categorias['hardware'],
            'icon': '🖥️',
            'descripcion': 'Servidor rack de última generación con procesadores Intel Xeon Scalable de 3ra Gen, ideal para virtualización y cargas de trabajo intensivas.',
            'precio': '$8,500',
            'precio_numerico': 8500.00,
            'fabricante': 'Dell',
            'modelo': 'PowerEdge R750',
            'destacado': True,
            'stock': 15,
            'features': [
                'Intel Xeon Scalable de 3ra Gen',
                'Hasta 2TB de RAM DDR4',
                'Almacenamiento hasta 32TB',
                'Gestión iDRAC9 integrada'
            ]
        },
        {
            'nombre': 'Cisco Catalyst 9300',
            'categoria': categorias['hardware'],
            'icon': '🔌',
            'descripcion': 'Switch empresarial de alto rendimiento con capacidades de seguridad avanzadas y automatización de red.',
            'precio': '$4,200',
            'precio_numerico': 4200.00,
            'fabricante': 'Cisco',
            'modelo': 'Catalyst 9300',
            'destacado': False,
            'stock': 25,
            'features': [
                '48 puertos Gigabit PoE+',
                'Uplinks de 40G',
                'DNA Center ready',
                'Seguridad avanzada integrada'
            ]
        },
        {
            'nombre': 'HPE ProLiant DL380 Gen10',
            'categoria': categorias['hardware'],
            'icon': '🔧',
            'descripcion': 'Servidor de propósito general líder en la industria con seguridad de clase mundial y rendimiento optimizado.',
            'precio': '$7,800',
            'precio_numerico': 7800.00,
            'fabricante': 'HPE',
            'modelo': 'ProLiant DL380 Gen10',
            'destacado': True,
            'stock': 10,
            'features': [
                'Intel Xeon o AMD EPYC',
                'Hasta 3TB de memoria',
                '12 ranuras PCIe',
                'HPE iLO 5 management'
            ]
        },
        
        # Software
        {
            'nombre': 'Microsoft 365 E5',
            'categoria': categorias['software'],
            'icon': '📊',
            'descripcion': 'Suite completa de productividad empresarial con seguridad avanzada, análisis y cumplimiento integrados.',
            'precio': '$57/usuario/mes',
            'precio_numerico': 57.00,
            'fabricante': 'Microsoft',
            'modelo': 'Microsoft 365 E5',
            'destacado': True,
            'stock': 9999,
            'features': [
                'Office 365 completo',
                'Seguridad y cumplimiento avanzados',
                'Power BI Pro incluido',
                'Teams con funciones premium'
            ]
        },
        {
            'nombre': 'Salesforce Sales Cloud',
            'categoria': categorias['software'],
            'icon': '💼',
            'descripcion': 'CRM líder mundial para gestión de ventas, automatización de marketing y análisis de clientes.',
            'precio': '$150/usuario/mes',
            'precio_numerico': 150.00,
            'fabricante': 'Salesforce',
            'modelo': 'Sales Cloud',
            'destacado': True,
            'stock': 9999,
            'features': [
                'Gestión completa de leads',
                'Automatización de ventas',
                'Einstein AI integrado',
                'Reportes y dashboards personalizados'
            ]
        },
        {
            'nombre': 'Adobe Creative Cloud',
            'categoria': categorias['software'],
            'icon': '🎨',
            'descripcion': 'Suite completa de herramientas creativas para diseño gráfico, video, web y fotografía profesional.',
            'precio': '$79.99/mes',
            'precio_numerico': 79.99,
            'fabricante': 'Adobe',
            'modelo': 'Creative Cloud All Apps',
            'destacado': False,
            'stock': 9999,
            'features': [
                'Photoshop, Illustrator, Premiere Pro',
                '100GB almacenamiento en nube',
                'Adobe Fonts completo',
                'Actualizaciones automáticas'
            ]
        },
        {
            'nombre': 'SAP S/4HANA',
            'categoria': categorias['software'],
            'icon': '📈',
            'descripcion': 'ERP inteligente de próxima generación con capacidades de IA y machine learning para empresas.',
            'precio': 'Desde $200/usuario/mes',
            'precio_numerico': 200.00,
            'fabricante': 'SAP',
            'modelo': 'S/4HANA',
            'destacado': False,
            'stock': 9999,
            'features': [
                'Base de datos in-memory',
                'IA y machine learning integrados',
                'Análisis en tiempo real',
                'Módulos financieros completos'
            ]
        },
        
        # Cloud
        {
            'nombre': 'AWS EC2 Enterprise',
            'categoria': categorias['cloud'],
            'icon': '☁️',
            'descripcion': 'Capacidad de cómputo escalable en la nube con más de 500 tipos de instancias para cualquier carga de trabajo.',
            'precio': 'Desde $0.096/hora',
            'precio_numerico': 0.096,
            'fabricante': 'Amazon Web Services',
            'modelo': 'EC2',
            'destacado': True,
            'stock': 9999,
            'features': [
                'Escalamiento automático',
                'Múltiples regiones globales',
                '99.99% de disponibilidad SLA',
                'Integración con servicios AWS'
            ]
        },
        {
            'nombre': 'Microsoft Azure Virtual Machines',
            'categoria': categorias['cloud'],
            'icon': '🌐',
            'descripcion': 'Máquinas virtuales flexibles con soporte para Windows y Linux, integración con servicios híbridos.',
            'precio': 'Desde $0.084/hora',
            'precio_numerico': 0.084,
            'fabricante': 'Microsoft',
            'modelo': 'Azure VMs',
            'destacado': True,
            'stock': 9999,
            'features': [
                'Windows y Linux',
                'Integración con Active Directory',
                'Azure Hybrid Benefit',
                'Backup automático incluido'
            ]
        },
        {
            'nombre': 'Google Cloud Platform',
            'categoria': categorias['cloud'],
            'icon': '📡',
            'descripcion': 'Plataforma cloud con infraestructura de Google, BigQuery para análisis y Kubernetes engine.',
            'precio': 'Desde $0.075/hora',
            'precio_numerico': 0.075,
            'fabricante': 'Google',
            'modelo': 'GCP Compute Engine',
            'destacado': False,
            'stock': 9999,
            'features': [
                'BigQuery integrado',
                'Google Kubernetes Engine',
                'AI y ML Platform',
                'Red global de Google'
            ]
        },
        {
            'nombre': 'Dropbox Business Advanced',
            'categoria': categorias['cloud'],
            'icon': '💾',
            'descripcion': 'Almacenamiento en nube empresarial con colaboración avanzada y controles de seguridad.',
            'precio': '$20/usuario/mes',
            'precio_numerico': 20.00,
            'fabricante': 'Dropbox',
            'modelo': 'Business Advanced',
            'destacado': False,
            'stock': 9999,
            'features': [
                'Almacenamiento ilimitado',
                'Compartir y colaborar',
                'Control de versiones 180 días',
                'Integración con Office 365'
            ]
        },
        
        # Seguridad
        {
            'nombre': 'Palo Alto Networks NGFW',
            'categoria': categorias['seguridad'],
            'icon': '🔒',
            'descripcion': 'Firewall de próxima generación con prevención de amenazas, URL filtering y análisis de malware.',
            'precio': '$4,500/año',
            'precio_numerico': 4500.00,
            'fabricante': 'Palo Alto Networks',
            'modelo': 'PA-Series',
            'destacado': True,
            'stock': 20,
            'features': [
                'Prevención de amenazas',
                'URL filtering avanzado',
                'SSL decryption',
                'WildFire cloud-based analysis'
            ]
        },
        {
            'nombre': 'CrowdStrike Falcon',
            'categoria': categorias['seguridad'],
            'icon': '🛡️',
            'descripcion': 'Plataforma EPP/EDR cloud-native con protección en tiempo real y threat hunting avanzado.',
            'precio': '$99.99/endpoint/año',
            'precio_numerico': 99.99,
            'fabricante': 'CrowdStrike',
            'modelo': 'Falcon',
            'destacado': True,
            'stock': 9999,
            'features': [
                'Protección endpoint en tiempo real',
                'EDR y threat hunting',
                'Machine learning prevention',
                'Respuesta automática'
            ]
        },
        {
            'nombre': 'Cisco Duo Security',
            'categoria': categorias['seguridad'],
            'icon': '🔐',
            'descripcion': 'Autenticación multifactor y acceso de confianza cero para proteger usuarios y aplicaciones.',
            'precio': '$3/usuario/mes',
            'precio_numerico': 3.00,
            'fabricante': 'Cisco',
            'modelo': 'Duo Security',
            'destacado': False,
            'stock': 9999,
            'features': [
                'Autenticación 2FA/MFA',
                'Single Sign-On',
                'Device Trust',
                'Integración con 100+ apps'
            ]
        },
        {
            'nombre': 'Fortinet FortiGate',
            'categoria': categorias['seguridad'],
            'icon': '🚨',
            'descripcion': 'Firewall empresarial con SD-WAN, seguridad de red completa y prevención de intrusiones.',
            'precio': '$3,200/año',
            'precio_numerico': 3200.00,
            'fabricante': 'Fortinet',
            'modelo': 'FortiGate',
            'destacado': False,
            'stock': 18,
            'features': [
                'SD-WAN integrado',
                'IPS y antimalware',
                'VPN SSL y IPSec',
                'Application control'
            ]
        },
    ]
    
    productos_creados = 0
    for producto_data in productos_data:
        features = producto_data.pop('features')
        producto, created = Producto.objects.get_or_create(
            nombre=producto_data['nombre'],
            defaults=producto_data
        )
        
        if created:
            # Crear características
            for idx, feature in enumerate(features):
                CaracteristicaProducto.objects.create(
                    producto=producto,
                    descripcion=feature,
                    orden=idx
                )
            productos_creados += 1
            print(f"  ✓ {producto.nombre}")
    
    print(f"✅ {productos_creados} productos nuevos creados")
    
    # Crear servicios
    print("\n🛠️  Creando servicios...")
    
    servicios_data = [
        {
            'nombre': 'Consultoría de Transformación Digital',
            'icon': '🎯',
            'descripcion': 'Análisis completo de tu infraestructura actual y roadmap personalizado para la transformación digital de tu empresa.',
            'precio': 'Desde $5,000',
            'precio_numerico': 5000.00,
            'duracion_estimada': '4-6 semanas',
            'nivel_complejidad': 'avanzado',
            'destacado': True,
        },
        {
            'nombre': 'Cloud Migration',
            'icon': '☁️',
            'descripcion': 'Migración segura y eficiente de tus aplicaciones y datos a AWS, Azure o Google Cloud con mínimo downtime.',
            'precio': 'Desde $8,000',
            'precio_numerico': 8000.00,
            'duracion_estimada': '6-12 semanas',
            'nivel_complejidad': 'empresarial',
            'destacado': True,
        },
        {
            'nombre': 'Ciberseguridad y Auditoría',
            'icon': '🔒',
            'descripcion': 'Evaluación de seguridad, penetration testing, y implementación de controles de seguridad según ISO 27001.',
            'precio': 'Desde $4,500',
            'precio_numerico': 4500.00,
            'duracion_estimada': '3-4 semanas',
            'nivel_complejidad': 'avanzado',
            'destacado': True,
        },
        {
            'nombre': 'DevOps y CI/CD',
            'icon': '⚙️',
            'descripcion': 'Implementación de pipelines automatizados, contenedores Docker, Kubernetes y mejores prácticas DevOps.',
            'precio': 'Desde $6,500',
            'precio_numerico': 6500.00,
            'duracion_estimada': '4-8 semanas',
            'nivel_complejidad': 'avanzado',
            'destacado': False,
        },
        {
            'nombre': 'Desarrollo de Software a Medida',
            'icon': '💻',
            'descripcion': 'Desarrollo de aplicaciones web, móviles y empresariales con tecnologías modernas y metodologías ágiles.',
            'precio': 'Desde $10,000',
            'precio_numerico': 10000.00,
            'duracion_estimada': '8-16 semanas',
            'nivel_complejidad': 'empresarial',
            'destacado': True,
        },
        {
            'nombre': 'Soporte IT 24/7',
            'icon': '🛠️',
            'descripcion': 'Soporte técnico continuo para tu infraestructura, aplicaciones y usuarios con SLA garantizado.',
            'precio': '$2,500/mes',
            'precio_numerico': 2500.00,
            'duracion_estimada': 'Continuo',
            'nivel_complejidad': 'intermedio',
            'destacado': False,
        },
        {
            'nombre': 'Business Intelligence y Analytics',
            'icon': '📊',
            'descripcion': 'Implementación de dashboards, reportes y análisis de datos con Power BI, Tableau o herramientas personalizadas.',
            'precio': 'Desde $7,000',
            'precio_numerico': 7000.00,
            'duracion_estimada': '6-10 semanas',
            'nivel_complejidad': 'avanzado',
            'destacado': False,
        },
        {
            'nombre': 'Automatización de Procesos (RPA)',
            'icon': '🤖',
            'descripcion': 'Automatización de tareas repetitivas con UiPath, Automation Anywhere para aumentar eficiencia operacional.',
            'precio': 'Desde $5,500',
            'precio_numerico': 5500.00,
            'duracion_estimada': '4-8 semanas',
            'nivel_complejidad': 'intermedio',
            'destacado': False,
        },
    ]
    
    servicios_creados = 0
    for servicio_data in servicios_data:
        servicio, created = Servicio.objects.get_or_create(
            nombre=servicio_data['nombre'],
            defaults=servicio_data
        )
        if created:
            servicios_creados += 1
            print(f"  ✓ {servicio.nombre}")
    
    print(f"✅ {servicios_creados} servicios nuevos creados")
    
    # Resumen
    print("\n" + "="*60)
    print("✅ Base de datos poblada exitosamente!")
    print("="*60)
    print(f"📁 Categorías: {Categoria.objects.count()}")
    print(f"📦 Productos: {Producto.objects.count()}")
    print(f"🛠️  Servicios: {Servicio.objects.count()}")
    print("="*60)


if __name__ == '__main__':
    poblar_base_datos()
