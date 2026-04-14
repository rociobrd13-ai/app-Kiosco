from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id         = Column(Integer, primary_key=True, index=True)
    fecha      = Column(DateTime, server_default=func.now())
    total      = Column(Float, nullable=False)
    estado     = Column(String(20), default="completada")  # completada / anulada

    # Relación con los detalles
    detalles   = relationship("DetalleVenta", back_populates="venta")


class DetalleVenta(Base):
    __tablename__ = "detalle_ventas"

    id               = Column(Integer, primary_key=True, index=True)
    venta_id         = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    producto_id      = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad         = Column(Integer, nullable=False)
    precio_unitario  = Column(Float, nullable=False)  # precio al momento de vender

    # Relaciones
    venta    = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto")
    