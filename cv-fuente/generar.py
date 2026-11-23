"""Genera el CV en español e inglés (HTML) con el formato del CV original.
Uso: python generar.py   -> crea cv-es.html y cv-en.html; luego se imprimen a PDF con Edge (ver imprimir.ps1)."""
import os
AQUI = os.path.dirname(os.path.abspath(__file__))

ICON = {
    'mail': '<svg viewBox="0 0 24 24"><path d="M2 5h20v14H2z" fill="none"/><path d="M2 6.5 12 13l10-6.5V5H2zM2 8.8V19h20V8.8l-10 6.5z"/></svg>',
    'phone': '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>',
    'pin': '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/></svg>',
    'gh': '<svg viewBox="0 0 24 24"><path d="M12 1.5a10.5 10.5 0 0 0-3.3 20.5c.5.1.7-.2.7-.5v-1.8c-2.9.6-3.5-1.4-3.5-1.4-.5-1.2-1.2-1.5-1.2-1.5-.9-.7.1-.6.1-.6 1 .1 1.6 1.1 1.6 1.1.9 1.6 2.5 1.1 3.1.9.1-.7.4-1.1.7-1.4-2.3-.3-4.8-1.2-4.8-5.2 0-1.1.4-2.1 1.1-2.8-.1-.3-.5-1.3.1-2.8 0 0 .9-.3 2.9 1.1a10 10 0 0 1 5.2 0c2-1.4 2.9-1.1 2.9-1.1.6 1.5.2 2.5.1 2.8.7.8 1.1 1.7 1.1 2.8 0 4-2.5 4.9-4.8 5.2.4.3.7 1 .7 2v2.9c0 .3.2.6.7.5A10.5 10.5 0 0 0 12 1.5z"/></svg>',
}

ES = dict(
    lang='es', title='CV Carolina Aranibar Huayta',
    location='Bolivia - Santa Cruz',
    h_summary='RESUMEN PROFESIONAL',
    summary='Desarrolladora Full Stack, egresada de Ingeniería en Sistemas. Construyo software a medida para negocios reales: ERPs, automatizaciones con WhatsApp e inteligencia artificial, catálogos B2B y plataformas web con React, Next.js, TypeScript, Node.js y PostgreSQL. Experiencia remota en un e-commerce de alto tráfico y evaluando agentes de IA para programación en inglés.',
    h_exp='EXPERIENCIA LABORAL',
    jobs=[
        ('Outlier', 'Evaluadora de agentes de IA para programación', '05/2026 – 09/2026', 'Remoto', [
            'Guié a dos agentes de IA por una misma tarea de software de varias etapas (IDE en la nube y terminal).',
            'Verifiqué cada etapa a mano y con pruebas en lugar de confiar en el “terminado” del agente, y escribí instrucciones para cerrar exactamente lo que faltaba.',
            'Califiqué ambos recorridos (corrección, comportamiento, comunicación, estilo) con justificaciones en inglés.']),
        ('Quicksell.store', 'Desarrolladora Full Stack', '01/2026 – 09/2026', 'Remoto', [
            'Migré el código heredado de JavaScript a TypeScript y las pruebas de React Testing Library a Vitest.',
            'Optimicé el rendimiento con carga diferida, división de código, optimización de imágenes y análisis de paquetes, y mejoré el SEO (metaetiquetas, datos estructurados, Core Web Vitals).',
            'Rediseñé los módulos de Comercio, Lista de seguimiento y Sorteo con componentes reutilizables, mejorando los flujos de conversión (Next.js, React, Node.js/Express).']),
        ('Accesorios Shirley', 'Desarrolladora de automatización e IA', '09/2025 – 11/2025', 'Freelance', [
            'Construí un agente de ventas para lives de TikTok: una IA de visión (Gemini) lee la captura que el comprador envía por WhatsApp y registra la venta.',
            'Llevé las reglas críticas (totales, estados, conciliación) a funciones y triggers de PostgreSQL y añadí la detección de comprobantes de pago reutilizados.',
            'Panel en tiempo real donde la vendedora solo confirma pagos (n8n, PostgreSQL, WhatsApp API, Docker).']),
        ('Dulzura Pastelería', 'Desarrolladora Full Stack', '05/2025 – 07/2025', 'Freelance', [
            'Desarrollé un ERP de pastelería con costeo por recetas y sub-recetas, inventario que se descuenta con cada venta y pedidos por WhatsApp vía n8n.',
            'Depuré los costos de varios Excel con fórmulas rotas y documenté más de 20 decisiones con la dueña.',
            'App de escritorio con SQLite local, respaldo automático por Gmail y actualización desde GitHub, para trabajar aunque falle internet (React, TypeScript, Node.js, Prisma).']),
        ('OtherBrain', 'Desarrolladora n8n', '01/2025 – 04/2025', '', [
            'Integré WhatsApp Business con n8n para enviar los pedidos directo al equipo de producción.',
            'Guardé datos en Supabase/PostgreSQL, sincronizados con Google Sheets para informes en tiempo real.',
            'Desarrollé paneles en React y TypeScript para visualizar el flujo de pedidos automatizados en tiempo real.']),
        ('Universal Tours LTDA.', 'Desarrolladora Frontend', '01/2024 – 03/2024', 'Freelance', [
            'Desarrollé una plataforma de asesoría y venta de viajes con destinos y paquetes (Punta Cana, Salvador de Bahía, Guarujá), integrando APIs de viajes de terceros.',
            'Diseñé el esquema de base de datos y la API para guardar las cotizaciones y gestionarlas desde un panel admin con autorización en cada acción (Next.js, TypeScript, Supabase).']),
        ('Teleserv Group', 'Desarrolladora Frontend', '01/2023 – 04/2023', 'Freelance', [
            'Catálogo B2B para un mayorista de fibra óptica y redes GPON: recorrido catálogo → ficha → cotización.',
            'Generé las fichas de forma estática para carga rápida y SEO, y protegí los formularios de contacto con Row Level Security (Next.js, TypeScript, Supabase).']),
    ],
    h_extra='PROYECTOS ADICIONALES',
    extra=[('No Country', 'Medicae · simulación laboral (hackathon), equipo de 4', '02/2026 – 03/2026', '', [
        'API REST en Python con Django por dominios (pacientes, turnos, documentos, pagos), paneles por rol en React con Material UI y PostgreSQL en Docker.'])],
    h_edu='EDUCACIÓN',
    edu=[('Universidad Aquino Bolivia (UDABOL)', 'Ingeniería en Sistemas (egresada, titulación en curso)', '01/2020 – 11/2023'),
         ('San Pablo Instituto', 'Certificado en Diseño Gráfico', '01/2019 – 07/2019')],
    h_skills='HABILIDADES/HERRAMIENTAS',
    skills=[('Frontend', 'React, Next.js, TypeScript, JavaScript, Tailwind CSS, HTML5, CSS3'),
            ('Backend', 'Node.js, Express, NestJS, Python, Django, REST APIs, Prisma'),
            ('Bases de datos', 'PostgreSQL, MongoDB, MySQL, Supabase, SQLite'),
            ('Automatización e IA', 'n8n, WhatsApp API, Gemini AI, Docker, Vercel')],
    h_lang='IDIOMAS',
    langs=[('Español', 'Nativo'), ('Inglés', 'EF SET 61/100 (julio 2026)')],
)

EN = dict(
    lang='en', title='Resume Carolina Aranibar Huayta',
    location='Santa Cruz, Bolivia',
    h_summary='PROFESSIONAL SUMMARY',
    summary='Full Stack Developer who has completed all coursework in Systems Engineering. I build custom software for real businesses: ERPs, WhatsApp and AI automations, B2B catalogs and web platforms with React, Next.js, TypeScript, Node.js and PostgreSQL. Remote experience on a high-traffic e-commerce platform and evaluating AI coding agents in English.',
    h_exp='WORK EXPERIENCE',
    jobs=[
        ('Outlier', 'AI Coding Agent Evaluator', '05/2026 – 09/2026', 'Remote', [
            'Guided two AI agents through the same multi-step software task (cloud IDE and terminal).',
            'Verified every step by hand and with tests instead of trusting the agent’s “done”, and wrote follow-up instructions to close exactly the gaps that were left.',
            'Graded both runs (correctness, behavior, communication, code style) with written justifications.']),
        ('Quicksell.store', 'Full Stack Developer', '01/2026 – 09/2026', 'Remote', [
            'Migrated legacy JavaScript code to TypeScript and the test suite from React Testing Library to Vitest.',
            'Improved performance with lazy loading, code splitting, image optimization and bundle analysis, and improved SEO (meta tags, structured data, Core Web Vitals).',
            'Redesigned the Commerce, Watchlist and Giveaway modules with reusable components, improving conversion flows (Next.js, React, Node.js/Express).']),
        ('Accesorios Shirley', 'Automation & AI Developer', '09/2025 – 11/2025', 'Freelance', [
            'Built a sales agent for TikTok live streams: a vision model (Gemini) reads the screenshot the buyer sends on WhatsApp and records the sale.',
            'Moved the critical rules (totals, statuses, reconciliation) into PostgreSQL functions and triggers and added detection of reused payment receipts.',
            'Real-time dashboard where the seller only confirms payments (n8n, PostgreSQL, WhatsApp API, Docker).']),
        ('Dulzura Pastelería', 'Full Stack Developer', '05/2025 – 07/2025', 'Freelance', [
            'Developed a bakery ERP with recipe and sub-recipe costing, inventory that updates with every sale, and WhatsApp orders through n8n.',
            'Cleaned up costs from spreadsheets with broken formulas and documented 20+ decisions with the owner.',
            'Desktop app with a local SQLite database, automatic Gmail backups and updates from GitHub, so it keeps working offline (React, TypeScript, Node.js, Prisma).']),
        ('OtherBrain', 'n8n Developer', '01/2025 – 04/2025', '', [
            'Integrated WhatsApp Business with n8n to route customer orders straight to the production team.',
            'Stored operational data in Supabase/PostgreSQL, synced with Google Sheets for real-time reporting.',
            'Built React and TypeScript dashboards to visualize the automated order flow in real time.']),
        ('Universal Tours LTDA.', 'Frontend Developer', '01/2024 – 03/2024', 'Freelance', [
            'Developed a travel advisory and booking platform with destinations and packages (Punta Cana, Salvador de Bahía, Guarujá), integrating third-party travel APIs.',
            'Designed the database schema and API to store quote requests and manage them from an admin panel with authorization on every action (Next.js, TypeScript, Supabase).']),
        ('Teleserv Group', 'Frontend Developer', '01/2023 – 04/2023', 'Freelance', [
            'B2B catalog for a fiber-optic and GPON equipment wholesaler: catalog → product page → quote flow.',
            'Generated product pages statically for fast loading and SEO, and protected contact forms with Row Level Security (Next.js, TypeScript, Supabase).']),
    ],
    h_extra='ADDITIONAL PROJECTS',
    extra=[('No Country', 'Medicae · job simulation (hackathon), team of 4', '02/2026 – 03/2026', '', [
        'Python REST API with Django split by domain (patients, shifts, documents, payments), role-based dashboards in React with Material UI, and PostgreSQL in Docker.'])],
    h_edu='EDUCATION',
    edu=[('Universidad Aquino Bolivia (UDABOL)', 'Systems Engineering (coursework completed, degree pending)', '01/2020 – 11/2023'),
         ('San Pablo Instituto', 'Graphic Design Certificate', '01/2019 – 07/2019')],
    h_skills='SKILLS/TOOLS',
    skills=[('Frontend', 'React, Next.js, TypeScript, JavaScript, Tailwind CSS, HTML5, CSS3'),
            ('Backend', 'Node.js, Express, NestJS, Python, Django, REST APIs, Prisma'),
            ('Databases', 'PostgreSQL, MongoDB, MySQL, Supabase, SQLite'),
            ('Automation & AI', 'n8n, WhatsApp API, Gemini AI, Docker, Vercel')],
    h_lang='LANGUAGES',
    langs=[('Spanish', 'Native'), ('English', 'EF SET 61/100 (July 2026)')],
)

CSS = """
@page{size:Letter;margin:0.36in 0.5in 0.3in}
*{box-sizing:border-box}
body{margin:0;font-family:'Source Sans 3','Source Sans Pro',Calibri,Arial,sans-serif;font-size:9.5pt;line-height:1.2;color:#111}
h1{font-size:20pt;margin:0 0 3px;font-weight:700;letter-spacing:-.2px}
.contact{display:flex;flex-wrap:wrap;gap:4px 20px;font-size:9.6pt;margin-bottom:6px}
.contact span{display:inline-flex;align-items:center;gap:6px}
.contact svg{width:11px;height:11px;fill:#111}
.contact a{color:#111;text-decoration:none}
h2{font-size:10.2pt;font-weight:700;margin:6px 0 3px;padding-bottom:2px;border-bottom:1.6px solid #111;letter-spacing:.2px}
p{margin:0}
.entry{display:flex;justify-content:space-between;gap:24px;margin-bottom:4px;break-inside:avoid}
.entry .l{flex:1}
.entry .r{text-align:right;white-space:nowrap}
ul{margin:1px 0 0;padding:0;list-style:none}
li{padding-left:10px;text-indent:-10px}
li::before{content:"- "}
.edu{display:flex;justify-content:space-between;margin-bottom:2px}
.skills b,.entry b,.edu b{font-weight:700}
.sep{display:inline-block;width:1px;height:11px;background:#999;margin:0 9px;vertical-align:-1px}
"""


def html(d):
    def entries(items):
        out = ''
        for co, role, dates, where, bullets in items:
            lis = ''.join(f'<li>{b}</li>' for b in bullets)
            r = dates + (f'<br>{where}' if where else '')
            out += f'<div class="entry"><div class="l"><b>{co},</b> <i>{role}</i><ul>{lis}</ul></div><div class="r">{r}</div></div>'
        return out
    edu = ''.join(f'<div class="edu"><span><b>{a},</b> <i>{b}</i></span><span>{c}</span></div>' for a, b, c in d['edu'])
    skills = '<span class="sep"></span>'.join(f'<b>{k}:</b> {v}' for k, v in d['skills'])
    langs = '<span class="sep"></span>'.join(f'<b>{k}:</b> {v}' for k, v in d['langs'])
    return f"""<!doctype html><html lang="{d['lang']}"><head><meta charset="utf-8"><title>{d['title']}</title>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,700;1,400&display=block" rel="stylesheet">
<style>{CSS}</style></head><body>
<h1>Carolina Aranibar Huayta</h1>
<div class="contact">
<span>{ICON['mail']}linaaranibar@gmail.com</span>
<span>{ICON['phone']}+591 61317418</span>
<span>{ICON['pin']}{d['location']}</span>
<span>{ICON['gh']}<a href="https://github.com/Lin4saurus">github.com/Lin4saurus</a></span>
</div>
<h2>{d['h_summary']}</h2><p>{d['summary']}</p>
<h2>{d['h_exp']}</h2>{entries(d['jobs'])}
<h2>{d['h_extra']}</h2>{entries(d['extra'])}
<h2>{d['h_edu']}</h2>{edu}
<h2>{d['h_skills']}</h2><p class="skills">{skills}</p>
<h2>{d['h_lang']}</h2><p>{langs}</p>
</body></html>"""


for d, name in ((ES, 'cv-es.html'), (EN, 'cv-en.html')):
    open(os.path.join(AQUI, name), 'w', encoding='utf-8').write(html(d))
print('ok')
