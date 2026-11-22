# CloudPath City · Expedición Nimbus

Una aventura de aprendizaje de Azure en una ciudad de píxeles. Explora con **Nimbus**, tu compañero nube, reúne insignias, construye un tenant simulado y defiéndelo del **Equipo Brecha**.

**[Jugar en GitHub Pages](https://jonathan171816.github.io/cloudpath-city/)** · [HTML autónomo](index.html)

El juego funciona en **un solo `index.html`**, con HTML5 Canvas, JavaScript puro y CSS. Fuentes y dibujos están incluidos: no requiere librerías, CDN, cuenta de Azure ni servidor de aplicación. Los enlaces de estudio sí requieren conexión.

## La expedición

| Ciudad | Ruta | Casas | Pisos | Banco de retos | Banco de azoteas | Banco de torre |
|---|---|---:|---:|---:|---:|---:|
| Villa Rubí | AZ-900 · Fundamentos | 6 | 13 | 130 | 60 | 40 |
| Ciudad Ámbar | AZ-104 · Administración | 5 | 15 | 180 | 50 | 40 |
| Ciudad Zafiro | AZ-305 · Arquitectura | 5 | 10 | 100 | 50 | 30 |
| **Total** | Hasta la Cima Celeste | **16** | **38** | **410** | **160** | **110** |

Son **680 preguntas originales** más **32 decisiones de defensa** en ocho incidentes. Los bancos de piso, azotea y torre son independientes. No se copian ni reformulan preguntas de bancos de examen. El material aportado como referencia de formato no se distribuye en este repositorio.

Cada casa organiza un módulo temático y cada piso, una unidad de aprendizaje:

1. **Estudio:** tarjetas, tablas, analogías «En la ciudad», consejos y enlaces al tema concreto con indicaciones de qué revisar.
2. **Reto:** cinco preguntas. Los fallos vuelven dentro del intento hasta responderlos correctamente. La puntuación registra la primera respuesta.
3. **Laboratorio**, en los pisos que lo incluyen: decisiones validadas, recursos visibles en el tenant y ejemplos de Azure CLI.
4. **Azotea:** cinco casos de integración exclusivos de esa casa. Se necesitan **4/5**; las respuestas se corrigen al terminar.
5. **Torre:** simulacro con casos exclusivos, corrección final y acceso a los pisos que necesitan repaso.

| Torre | Preguntas por intento | Mínimo del juego |
|---|---:|---:|
| AZ-900 | 20 | 14 |
| AZ-104 | 20 | 15 |
| AZ-305 | 15 | 11 |

Estos umbrales pertenecen al entrenamiento del juego y no reproducen la escala de puntuación de los exámenes oficiales. Las tres torres desbloquean el trofeo de aprendizaje de la Cima Celeste.

## Dificultad y rotación

- **AZ-900:** distinguir conceptos y responsabilidades ante restricciones concretas.
- **AZ-104:** operar y diagnosticar permisos, redes, almacenamiento, despliegues, monitoreo y recuperación.
- **AZ-305:** justificar arquitectura según costo, riesgo, recuperación y esfuerzo operativo.
- Los distractores tienen explicaciones individuales. La corrección identifica el requisito que decide el caso.
- Cada piso tiene un banco de **10 preguntas**; los de AZ-104 tienen **12**. Cada azotea dispone de **10 casos propios**.
- El selector excluye las preguntas del intento inmediatamente anterior y prioriza las menos vistas. Entre preguntas con la misma exposición, favorece los fallos pendientes.
- La selección se guarda al empezar: salir, volver a entrar o recargar también cambia el siguiente conjunto. El orden de las opciones se mezcla por separado.
- Los bancos son **finitos**: al reutilizar el banco reaparecerán casos anteriores. Los errores también reaparecen deliberadamente en el refuerzo y en **Mochila → Brechas**.
- Las torres reparten los casos entre las casas. Hay suficientes preguntas para dos simulacros consecutivos sin solapamiento.

## Laboratorios y defensas

Ocho laboratorios con **28 pasos** en total:

| Ruta | Laboratorio | Decisiones principales |
|---|---|---|
| AZ-900 | Mi primer tenant | Grupos de administración, suscripción, grupo de recursos y almacenamiento |
| AZ-104 | Identidad y gobierno | Grupo, RBAC, Policy, bloqueo, etiquetas y presupuesto |
| AZ-104 | Almacenamiento | Cuenta, contenedor privado, SAS y firewall |
| AZ-104 | Cómputo | VM, zona, tamaño, Bastion y extensión |
| AZ-104 | Redes | VNet hub, peering bidireccional y prioridades de NSG |
| AZ-104 | Monitoreo y respaldo | Log Analytics, alerta, backup y Site Recovery |
| AZ-305 | Landing zone | Ubicación de suscripciones, ámbitos de Policy y PIM |
| AZ-305 | Continuidad | Dependencias, RTO/RPO, recuperación y pruebas |

Los formularios rechazan decisiones incompatibles y explican el motivo. Las operaciones actualizan un árbol local de **tenant → grupos de administración → suscripciones → grupos de recursos → recursos**. Repetir un laboratorio no concede de nuevo su XP; con los mismos nombres y ámbitos actualiza los recursos simulados.

El script acumulado de **Mochila → Tenant** muestra ejemplos de comandos reales de Azure CLI y señala parámetros, identificadores y prerrequisitos pendientes. **El juego nunca ejecuta esos comandos ni despliega recursos en Azure.** Las plantillas deben revisarse y adaptarse antes de utilizarlas en un entorno real.

El Equipo Brecha ataca acceso anónimo, credenciales, SAS, acceso remoto, segmentación, copias de seguridad, gobierno y recuperación regional. Cada incidente tiene **cuatro decisiones y tres vidas**. Los servicios pueden quedar **operativos, caídos o expuestos**; el estado persiste si se abandona una defensa.

## Controles y experiencia visual

| Acción | Teclado | Pantalla táctil |
|---|---|---|
| Caminar | Flechas o WASD | D-pad |
| Hablar, entrar o avanzar diálogo | Espacio / Enter | A |
| Mochila | M | Mochila / B |
| Cerrar un panel | Escape | Botón del panel |
| Elegir respuesta | 1–4 o A–D | Tocar opción |

Baldosas de 16 px, cámara interpolada, Nimbus siguiendo la posición anterior del jugador, calles, plazas, canales, puentes, vegetación y techos por ciudad. El diario muestra la siguiente misión, la ruta, el atlas y las insignias. La interfaz se adapta a móvil, utiliza objetivos táctiles grandes y respeta `prefers-reduced-motion`.

El sonido usa Web Audio y comienza desactivado. Se puede cambiar desde la mochila. Los personajes, ciudades e insignias son dibujos originales hechos en código.

## Progreso, insignias y certificados

La mochila incluye **Ruta, Insignias, Tenant, Brechas, Intentos, Top y Certificados**.

- Guardado en `localStorage` con manejo de errores; no hay cuenta ni sincronización entre dispositivos.
- Nimbus conserva la clave `cloudpath-city-v2` para migrar XP, pisos, casas, laboratorios, recursos y certificados existentes. Reinicia los indicadores del banco antiguo para medir el aprendizaje con los nuevos casos.
- El historial conserva los últimos 80 intentos y separa la precisión inicial de los refuerzos.
- **Exportar progreso** descarga una copia JSON. Si el navegador no permite guardar, la interfaz lo indica.
- Las insignias son **logros educativos del juego**, no credenciales emitidas por Microsoft. El ranking es de ejemplo.
- Una puerta puede abrirse con un registro personal de certificado o con vista previa. El registro almacena el código o nombre del archivo en el navegador: no sube el documento ni verifica su autenticidad con Microsoft.
- Es posible añadir el certificado después de usar la vista previa.

## Código fuente y construcción

| Archivo | Responsabilidad |
|---|---|
| `src/data-az900.js` | Estudios, referencias y tres bancos de AZ-900 |
| `src/data-az104.js` | Estudios, referencias y tres bancos de AZ-104 |
| `src/data-az305.js` | Estudios, referencias y tres bancos de AZ-305 |
| `src/labs.js` | Formularios, validaciones, recursos y comandos |
| `src/incidents.js` | Incidentes, decisiones y estados de servicios |
| `src/world.js` | Arte, edificios, personajes, Nimbus e insignias |
| `src/engine.js` | Movimiento, progreso, preguntas, menú y flujo |
| `src/style.css`, `src/body.html` | Interfaz adaptable y estructura accesible |
| `assets/fonts/` | Fuentes integradas y licencias |
| `build.py` | Generador determinista del HTML autónomo |
| `tests/game.test.js`, `tests/mock-browser.js` | Pruebas de contenido, lógica y flujo |

Requisitos de desarrollo: **Python 3** y **Node.js 20 o posterior**. No hay paquetes que instalar.

```bash
python3 build.py
node --test tests/game.test.js
```

El build genera el mismo contenido en `index.html` y `dist/index.html`, con estilos, JavaScript y fuentes incorporados, además de `dist/.nojekyll`. Se puede abrir `index.html` directamente en un navegador moderno o servirlo como archivo estático.

Para añadir preguntas, sigue el formato de datos: enunciado, respuesta correcta, tres distractores, explicación y metadatos (`why`, `trap`, `refs`, `floor`, `level`). Las pruebas detectan enunciados duplicados, opciones repetidas, atribuciones inválidas y explicaciones ausentes. No reutilices preguntas entre las tres etapas.

## Verificación y publicación

Las pruebas automatizadas cubren los 680 casos, bancos separados, rotación entre intentos y recargas, refuerzo, azoteas y torres, migración, almacenamiento corrupto o bloqueado, puertas, rutas accesibles, Nimbus, certificados, menú y el flujo **estudio → reto → laboratorio → incidente → tenant**. También recorren los ocho laboratorios y su repetición.

La revisión en navegador complementa esas pruebas con tarjetas, opciones, explicaciones, D-pad, mochila y diseño en pantalla estrecha. La simulación de DOM de las pruebas no sustituye la comprobación visual.

El workflow `.github/workflows/static.yml`, al publicar en `main`, reconstruye, ejecuta las pruebas, verifica que el HTML generado coincida con el guardado en Git y despliega **solo `dist/`** en GitHub Pages. Los archivos de referencia y las pruebas no se incluyen en el artefacto web publicado.

## Fuentes de estudio y alcance

El contenido se organiza con las guías oficiales y documentación específica de Microsoft Learn. Las referencias por piso y caso se muestran dentro del juego.

- [Objetivos de AZ-900](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/az-900)
- [Objetivos de AZ-104](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
- [Objetivos de AZ-305](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/az-305)

Revisión de esta edición: **21 de noviembre de 2026**. Algunas referencias están en inglés para mantener acceso a documentación vigente. Microsoft puede modificar los objetivos, productos y rutas de documentación. El juego complementa el estudio y la práctica; no afirma cubrir exhaustivamente cada examen ni garantiza aprobarlo.

Las fuentes **Press Start 2P** y **VT323** se distribuyen con sus licencias SIL Open Font License en `assets/fonts/`. Proyecto educativo independiente, no afiliado a Microsoft ni a una franquicia de videojuegos.
