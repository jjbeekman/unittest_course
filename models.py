from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True, comment="Primary-key column is auto-incremented")
    name = Column(String, nullable=False)
    created_at = Column(DateTime(True), nullable=False, server_default=func.now())


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, comment="Primary-key column is auto-incremented")
    created_at = Column(DateTime(True), nullable=False, server_default=func.now())

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, comment="Primary-key column is auto-incremented")
    created_at = Column(DateTime(True), nullable=False, server_default=func.now())

    name = Column(String, nullable=False)
    shop_id = Column(ForeignKey("shops.id"), nullable=False, index=True)

    shop = relationship(Shop.__name__)
