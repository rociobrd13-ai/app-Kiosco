from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Archivo de la base de datos SQLite
# Se crea automáticamente en la carpeta del proyecto
DATABASE_URL = "sqlite:///./kiosco.db"

# Motor de conexión
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # necesario para SQLite
)

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para todos los modelos
Base = declarative_base()

# Función que da una sesión por cada request
def get_db():
    db = SessionLocal()
    try:
        yield db        # entrega la sesión
    finally:
        db.close()      # siempre cierra aunque haya error