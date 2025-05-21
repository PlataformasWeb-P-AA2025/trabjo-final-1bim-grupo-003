
# Mini Proyecto: FutRedX – La Red de Fútbol de la Premier League

## Contexto

Un grupo de estudiantes apasionados por el fútbol ha creado *FutRedX*, una red social ficticia dedicada exclusivamente a compartir opiniones, noticias y momentos sobre la **Premier League inglesa**. Los usuarios pueden publicar frases, comentar eventos deportivos, y reaccionar a las publicaciones de otros.

La base de datos de esta red social está en desarrollo, y tú, como desarrollador/a, debes analizar los datos disponibles y modelar las clases necesarias para implementarla correctamente.

---

## Archivos entregados

1. `usuarios_red_x.csv`: contiene **100 usuarios únicos** registrados en la red FutRedX.
2. `usuarios_publicaciones.csv`: contiene **100 frases únicas** generadas por estos usuarios sobre la Premier League.
3. `usuario_publicacion_emocion.csv`: contiene las emociones de los usuarios para los comentarios.

---

## Solución

A partir del análisis de los datos y los requerimientos de la red FutRedX, se debe construir un modelo de base de datos con SQLAlchemy que represente adecuadamente el funcionamiento de esta red social. Realizar la migración de datos de los **csv** a la base de datos generada.

---

## Requisitos funcionales

1. Cada **usuario** puede hacer muchas publicaciones.
2. Cada **publicación** pertenece a un solo usuario.
3. Cada usuario puede **reaccionar a muchas publicaciones** (propias o ajenas).
4. Cada publicación puede recibir **reacciones de muchos usuarios**.
5. Solo se permite **una reacción por usuario en cada publicación**.
6. La reacción debe tener un campo `tipo de emocion`.

---

## Tareas a realizar
0. **Usar el número de archivos de python** que se crea necesario.

1. **Diseñar las clases con el ORM SQLAlchemy** necesarias:
   - `Usuario`
   - `Publicacion`
   - `Reaccion` (como tabla intermedia)

2. **Analizar e importar los archivos CSV**:
   - Crear instancias de usuarios, publicaciones y reacciones

3. **Realizar consultas ORM útiles**:
   - Listar publicaciones de un usuario.
   - Listar las reacciones a una publicación.
   - Mostrar en qué publicaciones reaccionó un usuario.
   - Obtener un reporte de reacciones en función del número de veces que fueron usadas.
   - Listar todas las reacciones de tipo "alegre", "enojado", "pensativo" que sean de usuarios que cuyos nombre no inicien con vocal.
   - Crear 5 consultas adicionales

Las consultas debe estar documentadas / comentadas en cada archivo

---

## Sugerencia de clases ORM

```python
class Usuario
class Publicacion
class Reaccion
```

---

## Referente a la base de datos

- Usar una base de datos SQLite.
- Usar una base de datos Postgres a través de Docker.
---

## En caso de usar IA-Generativa para consulta de información

- En un archivo llamado informacion.md; explicando a detalle el uso de cada prompt

## Avanze 1 - 21/05/2025

- En el archivo "genera_base.py" creamos el modelo de la base de datos con las 3 clases "usuario","publicacion","reaccion" y en "reaccion" se le colocò la restriccion de que debe ser unico la combiancion de id_usuario y id_publicacion, ademàs a cada tabla le agregamos un campo "id" que serà autoincremental.

- Ademas se realizò la primera consulta en el archvio "consulta_publicaciones_usuario", donde se listan todas las publicaciones hechas por el usurio "William"

- En el archivo "ingreso_datos.py" creamos los engine y sesión y despues creamos el codigo para poder cargar los datos de los csv "usuarios_red_x.csv", "usuarios_publicaciones.csv", "usuario_publicacion_emocion.csv".
