const API_BASE_URL = 'http://localhost:8000/api';
let productosCache = [];
let serviciosCache = [];

async function cargarProductos(filtro = 'all') {
    const productosGrid = document.getElementById('productos-grid');
    productosGrid.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Cargando productos...</p>';

    try {
        let url = `${API_BASE_URL}/productos/`;
        if (filtro !== 'all') {
            url += `?categoria__nombre=${filtro}`;
        }

        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Error al cargar productos');
        }

        const data = await response.json();
        const productos = data.results || data;
        
        productosCache = productos;
        productosGrid.innerHTML = '';

        if (productos.length === 0) {
            productosGrid.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No hay productos disponibles en esta categoría.</p>';
            return;
        }

        productos.forEach(producto => {
            const card = document.createElement('div');
            card.className = 'producto-card';
            card.setAttribute('data-categoria', producto.categoria_nombre);
            
            const featuresHTML = producto.features && producto.features.length > 0
                ? producto.features.map(f => `<li>${f.descripcion}</li>`).join('')
                : '<li>Información próximamente</li>';
            
            card.innerHTML = `
                <div class="producto-icon">${producto.icon}</div>
                <h3>${producto.nombre}</h3>
                <span class="producto-category">${(producto.categoria_display || producto.categoria_nombre).toUpperCase()}</span>
                <p>${producto.descripcion}</p>
                <div class="producto-precio">${producto.precio}</div>
                <ul class="producto-features">
                    ${featuresHTML}
                </ul>
                <button class="btn btn-primary" onclick="verDetalles(${producto.id})">Ver Detalles</button>
            `;
            
            productosGrid.appendChild(card);
        });
    } catch (error) {
        console.error('Error al cargar productos:', error);
        productosGrid.innerHTML = `
            <p style="text-align: center; color: var(--warning-color);">
                ⚠️ Error al cargar productos. Asegúrate de que el servidor Django esté ejecutándose en ${API_BASE_URL}
                <br><br>
                <button class="btn btn-secondary" onclick="cargarProductos('all')">Reintentar</button>
            </p>
        `;
    }
}

async function cargarServicios() {
    const serviciosGrid = document.getElementById('servicios-grid');
    serviciosGrid.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Cargando servicios...</p>';

    try {
        const response = await fetch(`${API_BASE_URL}/servicios/`);
        if (!response.ok) {
            throw new Error('Error al cargar servicios');
        }

        const data = await response.json();
        const servicios = data.results || data;
        
        serviciosCache = servicios;
        serviciosGrid.innerHTML = '';

        if (servicios.length === 0) {
            serviciosGrid.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No hay servicios disponibles.</p>';
            return;
        }

        servicios.forEach(servicio => {
            const card = document.createElement('div');
            card.className = 'servicio-card';
            
            card.innerHTML = `
                <span class="servicio-icon">${servicio.icon}</span>
                <h3>${servicio.nombre}</h3>
                <p>${servicio.descripcion}</p>
                <div class="servicio-precio">${servicio.precio}</div>
                <button class="btn btn-secondary" onclick="contactarServicio('${servicio.nombre}', ${servicio.id})">Solicitar Cotización</button>
            `;
            
            serviciosGrid.appendChild(card);
        });
    } catch (error) {
        console.error('Error al cargar servicios:', error);
        serviciosGrid.innerHTML = `
            <p style="text-align: center; color: var(--warning-color);">
                ⚠️ Error al cargar servicios. Asegúrate de que el servidor Django esté ejecutándose en ${API_BASE_URL}
                <br><br>
                <button class="btn btn-secondary" onclick="cargarServicios()">Reintentar</button>
            </p>
        `;
    }
}

function setupFiltros() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            const filtro = button.getAttribute('data-filter');
            cargarProductos(filtro);
        });
    });
}

async function verDetalles(productoId) {
    try {
        const response = await fetch(`${API_BASE_URL}/productos/${productoId}/`);
        if (!response.ok) {
            throw new Error('Error al cargar detalles');
        }

        const producto = await response.json();
        const features = producto.features && producto.features.length > 0
            ? producto.features.map(f => `• ${f.descripcion}`).join('\n')
            : '• Información próximamente';

        alert(
            `${producto.nombre}\n\n` +
            `Categoría: ${producto.categoria_display}\n` +
            `Precio: ${producto.precio}\n\n` +
            `${producto.descripcion}\n\n` +
            `Características:\n${features}\n\n` +
            (producto.fabricante ? `Fabricante: ${producto.fabricante}\n` : '') +
            (producto.stock > 0 ? `Stock disponible: ${producto.stock}` : 'Consultar disponibilidad')
        );
    } catch (error) {
        console.error('Error al cargar detalles:', error);
        alert('Error al cargar los detalles del producto');
    }
}

function contactarServicio(nombreServicio, servicioId = null) {
    const form = document.querySelector('.contacto-form');
    form.scrollIntoView({ behavior: 'smooth' });
    
    if (servicioId) {
        form.setAttribute('data-servicio-id', servicioId);
    }
    
    setTimeout(() => {
        const textarea = form.querySelector('textarea');
        textarea.value = `Me interesa obtener una cotización para el servicio de ${nombreServicio}.`;
        textarea.focus();
    }, 500);
}

function setupMobileMenu() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const links = document.querySelectorAll('.nav-links a');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');
    });

    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });
}

function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
                const offsetTop = target.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

function setupScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    setTimeout(() => {
        document.querySelectorAll('.producto-card, .servicio-card, .estrategia-card').forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
            observer.observe(card);
        });
    }, 100);
}

function setupHeaderScroll() {
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            header.style.background = 'rgba(10, 15, 28, 0.98)';
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
        } else {
            header.style.background = 'rgba(10, 15, 28, 0.95)';
            header.style.boxShadow = 'none';
        }
    });
}

function setupFormulario() {
    const form = document.querySelector('.contacto-form');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const nombre = form.querySelector('input[type="text"]').value;
        const email = form.querySelector('input[type="email"]').value;
        const telefono = form.querySelector('input[type="tel"]').value;
        const mensaje = form.querySelector('textarea').value;
        
        const servicioId = form.getAttribute('data-servicio-id');
        const productoId = form.getAttribute('data-producto-id');
        
        const contactoData = {
            nombre,
            email,
            telefono: telefono || '',
            mensaje
        };
        
        if (servicioId) {
            contactoData.servicio_interes = parseInt(servicioId);
        }
        if (productoId) {
            contactoData.producto_interes = parseInt(productoId);
        }
        
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.disabled = true;
        submitBtn.textContent = 'Enviando...';
        
        try {
            const response = await fetch(`${API_BASE_URL}/contactos/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(contactoData)
            });
            
            if (!response.ok) {
                throw new Error('Error al enviar el mensaje');
            }
            
            const result = await response.json();
            
            alert(`¡Gracias ${nombre}!\n\n${result.message || 'Hemos recibido tu mensaje y nos pondremos en contacto contigo pronto.'}`);
            
            form.reset();
            form.removeAttribute('data-servicio-id');
            form.removeAttribute('data-producto-id');
            
        } catch (error) {
            console.error('Error al enviar contacto:', error);
            alert('Error al enviar el mensaje. Por favor, intenta nuevamente o contáctanos directamente por email.');
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    });
}

function animarContadores() {
    const contadores = document.querySelectorAll('.stat-number');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                entry.target.classList.add('counted');
                animarNumero(entry.target);
            }
        });
    }, { threshold: 0.5 });

    contadores.forEach(contador => observer.observe(contador));
}

function animarNumero(elemento) {
    const texto = elemento.textContent;
    const esNumero = /^\d+%?$/.test(texto);
    
    if (!esNumero) return;

    const valorFinal = parseInt(texto);
    const duracion = 2000;
    const pasos = 60;
    const incremento = valorFinal / pasos;
    let valorActual = 0;
    const intervalo = duracion / pasos;

    const timer = setInterval(() => {
        valorActual += incremento;
        if (valorActual >= valorFinal) {
            elemento.textContent = texto;
            clearInterval(timer);
        } else {
            elemento.textContent = Math.floor(valorActual) + (texto.includes('%') ? '%' : '');
        }
    }, intervalo);
}

function setupBusqueda() {
    const productosGrid = document.getElementById('productos-grid');
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const termino = e.target.value.toLowerCase();
            const cards = productosGrid.querySelectorAll('.producto-card');
            
            cards.forEach(card => {
                const nombre = card.querySelector('h3').textContent.toLowerCase();
                const descripcion = card.querySelector('p').textContent.toLowerCase();
                
                if (nombre.includes(termino) || descripcion.includes(termino)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Iniciando aplicación TI Digital...');
    console.log(`🔗 Conectando con API: ${API_BASE_URL}`);
    
    cargarProductos('all');
    cargarServicios();
    
    setupFiltros();
    setupMobileMenu();
    setupSmoothScroll();
    setupHeaderScroll();
    setupFormulario();
    setupBusqueda();
    
    setTimeout(() => {
        setupScrollAnimations();
        animarContadores();
    }, 300);
    
    console.log('✅ Aplicación inicializada');
    console.log('💡 Tip: Asegúrate de que el servidor Django esté ejecutándose en http://localhost:8000');
});

window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    
    if (hero && scrolled < 600) {
        hero.style.transform = `translateY(${scrolled * 0.4}px)`;
        hero.style.opacity = 1 - (scrolled / 600);
    }
});
