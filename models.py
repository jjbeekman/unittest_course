from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, UniqueConstraint, Boolean, text, \
    CheckConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True, comment="Primary-key column is auto-incremented")
    name = Column(String, nullable=False)
    created_at = Column(DateTime(True), nullable=False, server_default=func.now())


class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = (UniqueConstraint("phone_number"),)

    id = Column(Integer, primary_key=True, comment="Primary-key column is auto-incremented")
    created_at = Column(DateTime(True), nullable=False, server_default=func.now())

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (UniqueConstraint("shop_id", "name"),)

    id = Column(Integer, primary_key=True, comment="Primary-key column is auto-incremented")
    created_at = Column(DateTime(True), nullable=False, server_default=func.now())

    name = Column(String, nullable=False)
    shop_id = Column(ForeignKey("shops.id"), nullable=False, index=True)

    shop = relationship(Shop.__name__)


class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = (CheckConstraint("ordered_at < sla_at"),)

    id = Column(Integer, primary_key=True, comment="Primary-key column is auto-incremented")
    created_at = Column(DateTime(True), nullable=False, server_default=func.now())

    ordered_at = Column(DateTime(True), nullable=False)
    sla_at = Column(DateTime(True), nullable=False)  # Service-level agreement on last delivery date
    is_fulfilled = Column(Boolean, nullable=False, server_default=text("false"))
    product_id = Column(ForeignKey("products.id"), nullable=False, index=True)
    customer_id = Column(ForeignKey("customers.id"), nullable=False, index=True)

    product = relationship(Product.__name__)
    customer = relationship(Customer.__name__)
