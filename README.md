# eyfiber-social

Publicaciones automáticas de Ey.fiber en Facebook e Instagram.

Cada domingo por la tarde, una tarea programada de Claude prepara las publicaciones de la
semana (lunes, miércoles y viernes) y las programa en Metricool. A la hora de cada una,
Metricool envía un aviso al móvil para confirmarla.

## Qué hay aquí

- `GUIA.md`: servicios, tono, calendario y reglas. **Edítala para cambiar lo que se publica**
  (por ejemplo, para añadir una oferta en «Ofertas y precios vigentes»).
- `publicados.md`: registro de lo que ya se ha programado.
- `plantilla/post.html` y `render.py`: la plantilla de las imágenes.
- `imagenes/`: imágenes generadas cada semana (Metricool las descarga desde aquí).
- `propias/`: imágenes hechas a mano que se pueden reutilizar (app Mi línea, eSIM de viaje).
- `assets/logo.png`: el logo que lleva la plantilla (si no está, se escribe con texto).

El repositorio es público porque Metricool necesita descargar las imágenes. No subas aquí
nada privado.
