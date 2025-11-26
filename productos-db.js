// Base de datos de productos de TI actuales
const productosDB = [
    // Hardware
    {
        id: 1,
        nombre: "Dell PowerEdge R750",
        categoria: "hardware",
        icon: "🖥️",
        descripcion: "Servidor rack de última generación con procesadores Intel Xeon Scalable de 3ra Gen, ideal para virtualización y cargas de trabajo intensivas.",
        precio: "$8,500",
        features: [
            "Intel Xeon Scalable de 3ra Gen",
            "Hasta 2TB de RAM DDR4",
            "Almacenamiento hasta 32TB",
            "Gestión iDRAC9 integrada"
        ]
    },
    {
        id: 2,
        nombre: "Cisco Catalyst 9300",
        categoria: "hardware",
        icon: "🔌",
        descripcion: "Switch empresarial de alto rendimiento con capacidades de seguridad avanzadas y automatización de red.",
        precio: "$4,200",
        features: [
            "48 puertos Gigabit PoE+",
            "Uplinks de 40G",
            "DNA Center ready",
            "Seguridad avanzada integrada"
        ]
    },
    {
        id: 3,
        nombre: "HPE ProLiant DL380 Gen10",
        categoria: "hardware",
        icon: "🔧",
        descripcion: "Servidor de propósito general líder en la industria con seguridad de clase mundial y rendimiento optimizado.",
        precio: "$7,800",
        features: [
            "Intel Xeon o AMD EPYC",
            "Hasta 3TB de memoria",
            "12 ranuras PCIe",
            "HPE iLO 5 management"
        ]
    },

    // Software
    {
        id: 4,
        nombre: "Microsoft 365 E5",
        categoria: "software",
        icon: "📊",
        descripcion: "Suite completa de productividad empresarial con seguridad avanzada, análisis y cumplimiento integrados.",
        precio: "$57/usuario/mes",
        features: [
            "Office 365 completo",
            "Seguridad y cumplimiento avanzados",
            "Power BI Pro incluido",
            "Teams con funciones premium"
        ]
    },
    {
        id: 5,
        nombre: "Salesforce Sales Cloud",
        categoria: "software",
        icon: "💼",
        descripcion: "CRM líder mundial para gestión de ventas, automatización de marketing y análisis de clientes.",
        precio: "$150/usuario/mes",
        features: [
            "Gestión completa de leads",
            "Automatización de ventas",
            "Einstein AI integrado",
            "Reportes y dashboards personalizados"
        ]
    },
    {
        id: 6,
        nombre: "Adobe Creative Cloud",
        categoria: "software",
        icon: "🎨",
        descripcion: "Suite completa de herramientas creativas para diseño gráfico, video, web y fotografía profesional.",
        precio: "$79.99/mes",
        features: [
            "Photoshop, Illustrator, Premiere Pro",
            "100GB almacenamiento en nube",
            "Adobe Fonts completo",
            "Actualizaciones automáticas"
        ]
    },
    {
        id: 7,
        nombre: "SAP S/4HANA",
        categoria: "software",
        icon: "📈",
        descripcion: "ERP inteligente de próxima generación con capacidades de IA y machine learning para empresas.",
        precio: "Desde $200/usuario/mes",
        features: [
            "Base de datos in-memory",
            "IA y machine learning integrados",
            "Análisis en tiempo real",
            "Módulos financieros completos"
        ]
    },

    // Cloud
    {
        id: 8,
        nombre: "AWS EC2 Enterprise",
        categoria: "cloud",
        icon: "☁️",
        descripcion: "Capacidad de cómputo escalable en la nube con más de 500 tipos de instancias para cualquier carga de trabajo.",
        precio: "Desde $0.096/hora",
        features: [
            "Escalamiento automático",
            "Múltiples regiones globales",
            "99.99% de disponibilidad SLA",
            "Integración con servicios AWS"
        ]
    },
    {
        id: 9,
        nombre: "Microsoft Azure Virtual Machines",
        categoria: "cloud",
        icon: "🌐",
        descripcion: "Máquinas virtuales flexibles con soporte para Windows y Linux, integración con servicios híbridos.",
        precio: "Desde $0.084/hora",
        features: [
            "Windows y Linux",
            "Integración con Active Directory",
            "Azure Hybrid Benefit",
            "Backup automático incluido"
        ]
    },
    {
        id: 10,
        nombre: "Google Cloud Platform",
        categoria: "cloud",
        icon: "📡",
        descripcion: "Plataforma cloud con infraestructura de Google, BigQuery para análisis y Kubernetes engine.",
        precio: "Desde $0.075/hora",
        features: [
            "BigQuery integrado",
            "Google Kubernetes Engine",
            "AI y ML Platform",
            "Red global de Google"
        ]
    },
    {
        id: 11,
        nombre: "Dropbox Business Advanced",
        categoria: "cloud",
        icon: "💾",
        descripcion: "Almacenamiento en nube empresarial con colaboración avanzada y controles de seguridad.",
        precio: "$20/usuario/mes",
        features: [
            "Almacenamiento ilimitado",
            "Compartir y colaborar",
            "Control de versiones 180 días",
            "Integración con Office 365"
        ]
    },

    // Seguridad
    {
        id: 12,
        nombre: "Palo Alto Networks NGFW",
        categoria: "seguridad",
        icon: "🔒",
        descripcion: "Firewall de próxima generación con prevención de amenazas, URL filtering y análisis de malware.",
        precio: "$4,500/año",
        features: [
            "Prevención de amenazas",
            "URL filtering avanzado",
            "SSL decryption",
            "WildFire cloud-based analysis"
        ]
    },
    {
        id: 13,
        nombre: "CrowdStrike Falcon",
        categoria: "seguridad",
        icon: "🛡️",
        descripcion: "Plataforma EPP/EDR cloud-native con protección en tiempo real y threat hunting avanzado.",
        precio: "$99.99/endpoint/año",
        features: [
            "Protección endpoint en tiempo real",
            "EDR y threat hunting",
            "Machine learning prevention",
            "Respuesta automática"
        ]
    },
    {
        id: 14,
        nombre: "Cisco Duo Security",
        categoria: "seguridad",
        icon: "🔐",
        descripcion: "Autenticación multifactor y acceso de confianza cero para proteger usuarios y aplicaciones.",
        precio: "$3/usuario/mes",
        features: [
            "Autenticación 2FA/MFA",
            "Single Sign-On",
            "Device Trust",
            "Integración con 100+ apps"
        ]
    },
    {
        id: 15,
        nombre: "Fortinet FortiGate",
        categoria: "seguridad",
        icon: "🚨",
        descripcion: "Firewall empresarial con SD-WAN, seguridad de red completa y prevención de intrusiones.",
        precio: "$3,200/año",
        features: [
            "SD-WAN integrado",
            "IPS y antimalware",
            "VPN SSL y IPSec",
            "Application control"
        ]
    }
];

// Base de datos de servicios de TI
const serviciosDB = [
    {
        id: 1,
        nombre: "Consultoría de Transformación Digital",
        icon: "🎯",
        descripcion: "Análisis completo de tu infraestructura actual y roadmap personalizado para la transformación digital de tu empresa.",
        precio: "Desde $5,000"
    },
    {
        id: 2,
        nombre: "Cloud Migration",
        icon: "☁️",
        descripcion: "Migración segura y eficiente de tus aplicaciones y datos a AWS, Azure o Google Cloud con mínimo downtime.",
        precio: "Desde $8,000"
    },
    {
        id: 3,
        nombre: "Ciberseguridad y Auditoría",
        icon: "🔒",
        descripcion: "Evaluación de seguridad, penetration testing, y implementación de controles de seguridad según ISO 27001.",
        precio: "Desde $4,500"
    },
    {
        id: 4,
        nombre: "DevOps y CI/CD",
        icon: "⚙️",
        descripcion: "Implementación de pipelines automatizados, contenedores Docker, Kubernetes y mejores prácticas DevOps.",
        precio: "Desde $6,500"
    },
    {
        id: 5,
        nombre: "Desarrollo de Software a Medida",
        icon: "💻",
        descripcion: "Desarrollo de aplicaciones web, móviles y empresariales con tecnologías modernas y metodologías ágiles.",
        precio: "Desde $10,000"
    },
    {
        id: 6,
        nombre: "Soporte IT 24/7",
        icon: "🛠️",
        descripcion: "Soporte técnico continuo para tu infraestructura, aplicaciones y usuarios con SLA garantizado.",
        precio: "$2,500/mes"
    },
    {
        id: 7,
        nombre: "Business Intelligence y Analytics",
        icon: "📊",
        descripcion: "Implementación de dashboards, reportes y análisis de datos con Power BI, Tableau o herramientas personalizadas.",
        precio: "Desde $7,000"
    },
    {
        id: 8,
        nombre: "Automatización de Procesos (RPA)",
        icon: "🤖",
        descripcion: "Automatización de tareas repetitivas con UiPath, Automation Anywhere para aumentar eficiencia operacional.",
        precio: "Desde $5,500"
    }
];
