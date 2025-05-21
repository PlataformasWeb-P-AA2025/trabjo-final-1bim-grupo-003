from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario
from configuracion import cadena_base_datos

# Crear el engine para conectarse a la base de datos usando la cadena de conexión
engine = create_engine(cadena_base_datos)

# Crear una clase Session configurada con el engine
Session = sessionmaker(bind=engine)

# Instanciar una sesión para hacer consultas a la base de datos
session = Session()

# Nombre del usuario cuyas publicaciones queremos obtener
nombre_usuario = 'William'

# Buscar el primer usuario que coincida con el nombre dado
# .first() devuelve un solo objeto Usuario o None si no existe
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

print(f"Publicaciones de {nombre_usuario}:")

if usuario:
    # Si el usuario existe, recorrer la lista de publicaciones relacionadas
    for pub in usuario.publicaciones:
        print(pub.contenido)  # Imprimir el contenido de cada publicación
else:
    # Si no se encuentra el usuario, informar al usuario
    print("Usuario no encontrado")


