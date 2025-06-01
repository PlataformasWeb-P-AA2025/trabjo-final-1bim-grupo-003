from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def reacciones_a_publicacion(texto_publicacion):
    print(f"📌 Reacciones a la publicación:\n   '{texto_publicacion}'")
    publicacion = session.query(Publicacion).filter_by(contenido=texto_publicacion).first()
    if publicacion:
        for reaccion in publicacion.reacciones:
            print(f" - {reaccion.usuario.nombre}: {reaccion.tipo_emocion}")
    else:
        print("❌ Publicación no encontrada.")

if __name__ == "__main__":
    reacciones_a_publicacion("Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada.")
