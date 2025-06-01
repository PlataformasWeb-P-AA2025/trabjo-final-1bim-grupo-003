from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def publicaciones_de_usuario(nombre_usuario):
    print(f"📌 Publicaciones de {nombre_usuario}:")
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario:
        for pub in usuario.publicaciones:
            print(f" - {pub.contenido}")
    else:
        print("❌ Usuario no encontrado.")

# Ejecutar solo si se llama directamente
if __name__ == "__main__":
    publicaciones_de_usuario("Shelley")
#    publicaciones_de_usuario("Gabriella")

