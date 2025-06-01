from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def publicaciones_reaccionadas_por_usuario(nombre_usuario):
    print(f"📌 Publicaciones en las que {nombre_usuario} ha reaccionado:")
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario:
        for reaccion in usuario.reacciones:
            print(f" - '{reaccion.publicacion.contenido}' ({reaccion.tipo_emocion})")
    else:
        print("❌ Usuario no encontrado.")

if __name__ == "__main__":
    publicaciones_reaccionadas_por_usuario("Robert")
