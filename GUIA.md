# Guía de publicaciones de EYFiber

Esta guía la usa la tarea semanal que crea las publicaciones de Facebook e Instagram.
Juan Francisco puede editarla cuando quiera: lo que pongas aquí es lo que Claude usará.

## Quiénes somos

Ey.fiber es un operador de telecomunicaciones cercano, con base en Albacete y servicio en
Albacete, Cuenca, Castellón y Valencia (más de 50 pueblos, entre ellos Ledaña, Villamalea,
Fuentealbilla, Quintanar del Rey, Tarazona de la Mancha, Villarrobledo y Hellín).

Lema: «Internet que funciona. Personas que responden.»

## Servicios (solo hablar de estos)

- **Fibra simétrica** de hasta 1 Gb, con router e instalación incluidos.
- **Móvil**: líneas con datos acumulables y la app **Mi línea**.
- **App Mi línea** (gratis, Android e iPhone): ver los gigas que quedan, activar roaming y buzón,
  bloquear la línea si pierdes el móvil, contratar eSIM de viaje. Web: eyfiber.es/mi-linea
- **eSIM de viaje**: datos en el extranjero desde la app, sin cambiar de tarjeta SIM; se paga en la factura.
- **TV** básica y premium.
- **Alarmas y videovigilancia**.
- **Empresas (EyFiber Empresas)**: conexión, IP fija, redes MikroTik, VPN, seguridad y
  videovigilancia, sobre todo para el sector agroalimentario y polígonos (Campollano, Romica).
- **Hoteles y alojamientos (EyStay)**: wifi y tecnología para hoteles, casas rurales y
  apartamentos turísticos.

## Ofertas y precios vigentes

<!-- Juan Francisco: escribe aquí las ofertas que quieras anunciar, con fecha de fin.
     Si esta sección está vacía, las publicaciones NO mencionan precios ni promociones. -->

(ninguna)

## Contacto (usar tal cual)

- WhatsApp: 621 14 61 13 (todos los días, de 8:00 a 22:00)
- Teléfono: 967 97 78 07
- Web: eyfiber.es
- Instagram: @eyfiber.es

## Tono

- De tú, cercano y directo. Frases cortas. Como habla alguien del pueblo que sabe de redes.
- Hablar de situaciones reales: teletrabajo, la cooperativa, la casa rural en temporada, los
  chavales jugando online, el campo, la feria del pueblo.
- Sin exageraciones ni promesas técnicas que no podamos garantizar («nunca se cae», «la más rápida»).
- Sin tecnicismos salvo en publicaciones para empresas, y aun así explicados.
- Nada de política, religión, fútbol ni temas polémicos. No mencionar a la competencia.

## Calendario semanal

| Día       | Público                 | Temas posibles                                                     |
|-----------|-------------------------|--------------------------------------------------------------------|
| Lunes     | Para tu casa            | Fibra, móvil, app Mi línea, TV, alarmas, consejos de wifi en casa  |
| Miércoles | Para tu empresa         | EyFiber Empresas, agroalimentario, polígonos, seguridad, IP fija   |
| Viernes   | Para tu alojamiento / Cerca de ti | EyStay, casas rurales, eSIM de viaje, pueblos con cobertura, el equipo |

## Formato de cada publicación

- **Texto (pie de foto)**: 50–120 palabras. Primera línea que enganche. Una sola llamada a la
  acción al final (WhatsApp o eyfiber.es). Máximo 3 emojis. 3–6 hashtags al final, locales y
  del servicio (#Albacete #Cuenca #LaManchuela #fibraóptica #internetrural ...).
- **Imagen**: 1080x1350 generada con `render.py`:
  - `--publico`: «Para tu casa», «Para tu empresa», «Para tu alojamiento» o «Cerca de ti».
  - `--titulo`: máximo 9 palabras, en minúsculas salvo la primera letra, con punto final.
  - `--sub`: una o dos frases, máximo 22 palabras.
  - `--semilla`: un número distinto cada vez (por ejemplo el día del año).
- Si el tema es la app Mi línea o la eSIM de viaje, se puede usar una imagen de `propias/`
  en lugar de generar una (las cuadradas de 1080x1080).

## Lo que nunca se hace

- Inventar precios, promociones, velocidades, plazos de instalación o coberturas concretas.
- Usar datos de clientes reales o nombrar clientes sin permiso.
- Repetir el tema o el titular de las últimas 6 publicaciones (ver `publicados.md`).
