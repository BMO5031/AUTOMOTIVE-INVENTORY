# vehicle_inventory_cli/models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
# Initialize the database engine and session
DATABASE_URL = "sqlite:///vehicles.db"  # SQLite for simplicity
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    price = Column(Integer)

    # Define a one-to-many relationship to transactions
    transactions = relationship("Transaction", back_populates="vehicle")

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    transaction_date = Column(Date)  
    #transaction_figure = Column(Float, nullable=False) 

    # Define relationship to vehicle and customer
    vehicle = relationship("Vehicle", back_populates="transactions")
    customer = relationship("Customer", back_populates="transactions")

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)

    # Define relationship to transactions
    transactions = relationship("Transaction", back_populates="customer")
