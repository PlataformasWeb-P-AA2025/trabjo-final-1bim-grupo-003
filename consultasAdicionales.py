from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Usuarios con más de 2 publicaciones
def usuarios_con_muchas_publicaciones():
    print("📌 Usuarios con más de 2 publicaciones:")
    resultados = (
        session.query(Usuario)
        .join(Publicacion)
        .group_by(Usuario.id)
        .having(func.count(Publicacion.id) > 2)
        .all()
    )
    for usuario in resultados:
        print(f" - {usuario.nombre} ({len(usuario.publicaciones)} publicaciones)")

# 2. Publicaciones que tienen 3 o más reacciones
def publicaciones_con_varias_reacciones():
    print("📌 Publicaciones con 3 o más reacciones:")
    resultados = (
        session.query(Publicacion, func.count(Reaccion.id).label("total"))
        .join(Reaccion)
        .group_by(Publicacion.id)
        .having(func.count(Reaccion.id) >= 3)
        .all()
    )
    for publicacion, total in resultados:
        print(f" - '{publicacion.contenido}' ({total} reacciones)")

# 3. Usuarios que reaccionaron a sus propias publicaciones
def usuarios_reaccionaron_a_si_mismos():
    print("📌 Usuarios que reaccionaron a sus propias publicaciones:")
    resultados = (
        session.query(Reaccion)
        .join(Publicacion)
        .filter(Reaccion.usuario_id == Publicacion.usuario_id)
        .all()
    )
    for reaccion in resultados:
        print(f" - {reaccion.usuario.nombre} reaccionó a su publicación: '{reaccion.publicacion.contenido}' ({reaccion.tipo_emocion})")

# 4. Publicación con más reacciones
def publicacion_con_mas_reacciones():
    print("📌 Publicación con más reacciones:")
    resultado = (
        session.query(Publicacion, func.count(Reaccion.id).label("total"))
        .join(Reaccion)
        .group_by(Publicacion.id)
        .order_by(func.count(Reaccion.id).desc())
        .first()
    )
    if resultado:
        publicacion, total = resultado
        print(f" - '{publicacion.contenido}' con {total} reacciones")
    else:
        print("❌ No hay publicaciones con reacciones.")

# 5. Emociones más usadas por un usuario específico
def emociones_mas_usadas_por_usuario(nombre_usuario):
    print(f"📌 Emociones más usadas por {nombre_usuario}:")
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if not usuario:
        print("❌ Usuario no encontrado.")
        return
    resultados = (
        session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion))
        .filter(Reaccion.usuario_id == usuario.id)
        .group_by(Reaccion.tipo_emocion)
        .order_by(func.count(Reaccion.tipo_emocion).desc())
        .all()
    )
    if resultados:
        for emocion, total in resultados:
            print(f" - {emocion}: {total}")
    else:
        print("⚠️ Este usuario no tiene reacciones registradas.")

# Ejecutar solo si se llama directamente
if __name__ == "__main__":
    usuarios_con_muchas_publicaciones()
    print("--"*50)
    publicaciones_con_varias_reacciones()
    print("--"*50)
    usuarios_reaccionaron_a_si_mismos()
    print("--"*50)
    publicacion_con_mas_reacciones()
    print("--"*50)
    emociones_mas_usadas_por_usuario("Robert")
