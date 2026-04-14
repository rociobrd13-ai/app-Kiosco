from fastapi import FastAPI
from app.database import engine, Base

# Importar los modelos para que SQLAlchemy los registre
from app.models import producto, venta

# Crear las tablas en la base de datos automáticamente
Base.metadata.create_all(bind=engine)

# Crear la aplicación
app = FastAPI(
    title="Kiosco App API",
    description="Backend para la app de gestión de kioscos",
    version="1.0.0"
)

# Endpoint de prueba
@app.get("/")
def health_check():
    return {
        "status": "ok",
        "mensaje": "Bienvenida a la API del Kiosco 🏪"
    }