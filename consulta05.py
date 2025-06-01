from sqlalchemy import create_engine, and_, not_
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion, Usuario
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def reacciones_usuarios_no_vocales():
    print("📌 Reacciones 'alegre', 'enojado', 'pensativo' de usuarios cuyo nombre no inicia con vocal:")
    vocales = ('A', 'E', 'I', 'O', 'U')
    condiciones = [not_(Usuario.nombre.ilike(f"{v}%")) for v in vocales]
    filtro_no_vocal = and_(*condiciones)
    
    reacciones = (
        session.query(Reaccion)
        .join(Usuario)
        .filter(Reaccion.tipo_emocion.in_(["alegre", "enojado", "pensativo"]))
        .filter(filtro_no_vocal)
        .all()
    )
    for reaccion in reacciones:
        print(f" - {reaccion.usuario.nombre} → '{reaccion.publicacion.contenido}' ({reaccion.tipo_emocion})")

if __name__ == "__main__":
    reacciones_usuarios_no_vocales()
