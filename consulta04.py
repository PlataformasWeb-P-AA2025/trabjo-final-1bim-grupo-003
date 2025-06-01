from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def reporte_emociones():
    print("📌 Recuento de emociones usadas:")
    resultados = (
        session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion))
        .group_by(Reaccion.tipo_emocion)
        .order_by(func.count(Reaccion.tipo_emocion).desc())
        .all()
    )
    for emocion, total in resultados:
        print(f" - {emocion}: {total} veces")

if __name__ == "__main__":
    reporte_emociones()
