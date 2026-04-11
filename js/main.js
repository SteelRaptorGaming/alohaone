/* ============================================================
   AlohaOne Marketing Site — Main JS
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ---- Navbar scroll effect ----
    const navbar = document.querySelector('.navbar');
    const onScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 40);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // ---- Smooth-scroll for anchor links ----
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', e => {
            const target = document.querySelector(link.getAttribute('href'));
            if (!target) return;
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            // collapse mobile nav
            const collapse = document.querySelector('.navbar-collapse.show');
            if (collapse) bootstrap.Collapse.getOrCreateInstance(collapse).hide();
        });
    });

    // ---- Intersection Observer — fade-in on scroll ----
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });

    document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

    // ---- Early access form ----
    document.querySelectorAll('.early-access-form').forEach(form => {
        form.addEventListener('submit', e => {
            e.preventDefault();
            const input = form.querySelector('input[type="email"]');
            const btn = form.querySelector('button');
            const email = input.value.trim();
            if (!email) return;

            btn.disabled = true;
            btn.innerHTML = '<i class="fas fa-check me-1"></i> You\'re on the list!';
            btn.classList.replace('btn-primary-custom', 'btn-success');
            input.disabled = true;

            // TODO: POST to API endpoint
            console.log('Early access signup:', email);
        });
    });

    // ---- Year in footer ----
    const yearEl = document.getElementById('footer-year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // ---- Hero brain visualization ----
    renderBrainViz();
});

/* ============================================================
   Brain Visualization
   ------------------------------------------------------------
   Single source of truth for the hero neural network.
   To add a new platform: append one entry to PLATFORMS below.
   x/y are in viewBox coordinates (0-620 wide, 0-700 tall).
   Place new dots in any empty space — connections + icon
   placement happen automatically.
   ============================================================ */

const BRAIN_VIEWBOX = { w: 620, h: 700 };
const NEIGHBORS_PER_NODE = 3;  // each neuron connects to its N nearest

const PLATFORMS = [
    // Lower-mid wings (relocated from outer crown for visual balance)
    { slug: 'message',      name: 'Message',      icon: 'fa-comments',        color: '#22d3ee', x: 90,  y: 450 },
    { slug: 'assistant',    name: 'Assistant',    icon: 'fa-phone-volume',    color: '#c084fc', x: 570, y: 450 },

    // Top crown — flagship + AI
    { slug: 'cms',          name: 'CMS',          icon: 'fa-window-maximize', color: '#fb7185', x: 135, y: 115 },
    { slug: 'commerce',     name: 'Commerce',     icon: 'fa-shopping-cart',   color: '#22d3ee', x: 220, y: 80  },
    { slug: 'agent',        name: 'Agent',        icon: 'fa-robot',           color: '#c084fc', x: 320, y: 60  },
    { slug: 'crm',          name: 'CRM',          icon: 'fa-users',           color: '#34d399', x: 425, y: 85  },

    // Upper band
    { slug: 'inventory',    name: 'Inventory',    icon: 'fa-warehouse',       color: '#06b6d4', x: 130, y: 200 },
    { slug: 'document',     name: 'Document',     icon: 'fa-file-alt',        color: '#a78bfa', x: 245, y: 185 },
    { slug: 'marketing',    name: 'Marketing',    icon: 'fa-bullhorn',        color: '#fbbf24', x: 380, y: 175 },
    { slug: 'backup',       name: 'Backup',       icon: 'fa-shield-alt',      color: '#2dd4bf', x: 500, y: 185 },
    { slug: 'drive',        name: 'Drive',        icon: 'fa-cloud',           color: '#60a5fa', x: 560, y: 240 },

    // Mid band
    { slug: 'deliver',      name: 'Deliver',      icon: 'fa-truck-fast',      color: '#fb923c', x: 75,  y: 285 },
    { slug: 'case',         name: 'Case',         icon: 'fa-gavel',           color: '#818cf8', x: 200, y: 275 },
    { slug: 'social',       name: 'Social',       icon: 'fa-share-nodes',     color: '#f472b6', x: 320, y: 290 },
    { slug: 'email',        name: 'Email',        icon: 'fa-envelope',        color: '#fb923c', x: 440, y: 275 },
    { slug: 'affiliate',    name: 'Affiliate',    icon: 'fa-handshake',       color: '#facc15', x: 555, y: 320 },

    // Lower-mid band
    { slug: 'project',      name: 'Project',      icon: 'fa-diagram-project', color: '#818cf8', x: 140, y: 390 },
    { slug: 'support',      name: 'Support',      icon: 'fa-headset',         color: '#38bdf8', x: 265, y: 400 },
    { slug: 'configurator', name: 'Configure',    icon: 'fa-cube',            color: '#f472b6', x: 390, y: 385 },
    { slug: 'survey',       name: 'Survey',       icon: 'fa-poll',            color: '#22d3ee', x: 510, y: 400 },

    // Lower band
    { slug: 'knowledge',    name: 'Knowledge',    icon: 'fa-book-open',       color: '#c084fc', x: 180, y: 500 },
    { slug: 'training',     name: 'Training',     icon: 'fa-graduation-cap',  color: '#4ade80', x: 320, y: 515 },
    { slug: 'data',         name: 'Data',         icon: 'fa-database',        color: '#38bdf8', x: 430, y: 500 },

    // Bottom — foundation
    { slug: 'search',       name: 'Search',       icon: 'fa-magnifying-glass', color: '#5eead4', x: 310, y: 610 },

    // Lower-left wing
    { slug: 'browser',      name: 'Browser',      icon: 'fa-compass',         color: '#38bdf8', x: 90,  y: 560 },
];

function renderBrainViz() {
    const root = document.getElementById('brainViz');
    if (!root) return;

    const synapsesGroup = root.querySelector('.synapses');
    const neuronsGroup  = root.querySelector('.neurons');
    const iconsLayer    = root.querySelector('.hero-app-icons');
    if (!synapsesGroup || !neuronsGroup || !iconsLayer) return;

    const SVG_NS = 'http://www.w3.org/2000/svg';

    // ---- Build synapses (each neuron → its N nearest neighbors) ----
    const seen = new Set();
    PLATFORMS.forEach((p, i) => {
        const ranked = PLATFORMS
            .map((q, j) => ({ j, d: Math.hypot(p.x - q.x, p.y - q.y) }))
            .filter(o => o.j !== i)
            .sort((a, b) => a.d - b.d);

        for (let k = 0; k < NEIGHBORS_PER_NODE && k < ranked.length; k++) {
            const j = ranked[k].j;
            const key = i < j ? `${i}-${j}` : `${j}-${i}`;
            if (seen.has(key)) continue;
            seen.add(key);

            const line = document.createElementNS(SVG_NS, 'line');
            line.setAttribute('class', 'synapse');
            line.setAttribute('x1', p.x);
            line.setAttribute('y1', p.y);
            line.setAttribute('x2', PLATFORMS[j].x);
            line.setAttribute('y2', PLATFORMS[j].y);
            synapsesGroup.appendChild(line);
        }
    });

    // ---- Build neurons (glowing dots at each platform position) ----
    PLATFORMS.forEach(p => {
        const c = document.createElementNS(SVG_NS, 'circle');
        c.setAttribute('class', 'neuron');
        c.setAttribute('cx', p.x);
        c.setAttribute('cy', p.y);
        c.setAttribute('r', 5);
        c.style.fill = p.color;
        c.style.filter = `drop-shadow(0 0 5px ${p.color})`;
        neuronsGroup.appendChild(c);
    });

    // ---- Build icon overlay (icon + label hanging below each neuron) ----
    PLATFORMS.forEach(p => {
        const left = (p.x / BRAIN_VIEWBOX.w) * 100;
        const top  = (p.y / BRAIN_VIEWBOX.h) * 100;

        const wrap = document.createElement('div');
        wrap.className = 'hero-app-icon-wrap';
        wrap.style.left = `${left}%`;
        wrap.style.top  = `${top}%`;

        wrap.innerHTML = `
            <a href="platforms/${p.slug}.html" class="hero-app-icon" title="Aloha${p.name}">
                <i class="fas ${p.icon}" style="color:${p.color}"></i>
                <span>${p.name}</span>
            </a>
        `;
        iconsLayer.appendChild(wrap);
    });
}
