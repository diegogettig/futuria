# FUTURIA — Configuración Cloudflare para futuria.institute

## Objetivo
Dejar Cloudflare configurado con:
- Correo profesional (Google Workspace)
- Web deployada (Vercel/Netlify)
- Newsletter (Beehiiv)
- SSL activo
- Seguridad básica

---

## PARTE 1 — Verificar estado del dominio en Cloudflare

1. Entrar a https://dash.cloudflare.com
2. Si aparece `futuria.institute` con estado **Active**, continuar
3. Si aparece **Pending**: esperar a que cambie a Active (24-48hs desde que cambiaste nameservers en Namecheap)

---

## PARTE 2 — DNS Records ( agregar estos registros )

Dentro de Cloudflare → DNS → Add record:

### A — Web principal (Vercel)
| Tipo | Nombre | Contenido | Proxy |
|---|---|---|---|
| A | @ | 76.76.21.21 | ☁️ Naranja (proxied) |

### CNAME — www
| Tipo | Nombre | Contenido | Proxy |
|---|---|---|---|
| CNAME | www | cname.vercel-dns.com | ☁️ Naranja (proxied) |

### MX — Google Workspace (5 registros)
| Tipo | Nombre | Contenido | Prioridad | Proxy |
|---|---|---|---|---|
| MX | @ | ASPMX.L.GOOGLE.COM | 1 | ☁️ Nube gris (DNS only) |
| MX | @ | ALT1.ASPMX.L.GOOGLE.COM | 5 | ☁️ Gris |
| MX | @ | ALT2.ASPMX.L.GOOGLE.COM | 5 | ☁️ Gris |
| MX | @ | ALT3.ASPMX.L.GOOGLE.COM | 10 | ☁️ Gris |
| MX | @ | ALT4.ASPMX.L.GOOGLE.COM | 10 | ☁️ Gris |

### TXT — SPF (Google Workspace)
| Tipo | Nombre | Contenido | Proxy |
|---|---|---|---|
| TXT | @ | v=spf1 include:_spf.google.com ~all | ☁️ Gris |

### TXT — DKIM (Google Workspace)
Después de crear la cuenta Google Workspace, Google te dará 2-3 valores DKIM. Agrégales como TXT records con nombre `google._domainkey` y `google._domainkey2` etc.

### TXT — DMARC
| Tipo | Nombre | Contenido | Proxy |
|---|---|---|---|
| TXT | @ | v=DMARC1; p=none; rua=mailto:hola@futuria.institute | ☁️ Gris |

### CNAME — Beehiiv (newsletter)
| Tipo | Nombre | Contenido | Proxy |
|---|---|---|---|
| CNAME | newsletter | custom.beehiiv.com | ☁️ Naranja |

### CNAME — Vercel (confirmación)
| Tipo | Nombre | Contenido | Proxy |
|---|---|---|---|
| CNAME | www | cname.vercel-dns.com | ☁️ Naranja |

---

## PARTE 3 — SSL/TLS

1. Cloudflare → SSL/TLS
2. Elegir **Full (strict)**
3. Activar **Always Use HTTPS**
4. Activar **HTTP/2**
5. Activar **Automatic HTTPS Rewrites**

---

## PARTE 4 — Seguridad básica

1. Cloudflare → Security → Settings:
   - Security Level: Medium
   - Challenge Passage: 30 minutos
   - Activar "I'm Under Attack" mode solo si hay ataque real

2. Cloudflare → Speed → Optimization:
   - Auto Minify: JS, CSS, HTML → ON
   - Brotli: ON
   - Rocket Loader: OFF (puede romper scripts de la web)
   - Mirage: OFF (no necesario para contenido estático)

---

## PARTE 5 — Después de agregar los registros DNS

Esperar 5-10 minutos para que Cloudflare propague.
Verificar:
- `https://futuria.institute` carga la web
- `https://newsletter.futuria.institute` muestra página de Beehiiv
- `hola@futuria.institute` recibe emails (después de configurar Google Workspace)

---

## PARTE 6 — Google Workspace (siguiente paso)

1. Entrar a https://workspace.google.com
2. Crear cuenta: "Usar un dominio que ya tengo"
3. Escribir: `futuria.institute`
4. Seguir pasos de verificación (Cloudflare generará registros TXT para verificar dominio)
5. Crear usuarios:
   - `hola@futuria.institute` (general, newsletter)
   - `diego@futuria.institute` (personal)
   - `dg@futuria.institute` (Director General IA)
   - `equipo@futuria.institute` (operaciones)

---

*Documento preparado por: Director General IA (Hermes/FUTURIA)*
*Fecha: Junio 2026*
*Estado: Pendiente activación cuando Cloudflare muestre "Active"*
