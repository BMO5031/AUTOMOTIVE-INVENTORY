# vehicle_inventory_cli/cli.py
import click
from models import SessionLocal, Vehicle, Transaction, Customer, Base
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command()
@click.option('--make', prompt='Enter the make of the vehicle')
@click.option('--model', prompt='Enter the model of the vehicle')
@click.option('--year', prompt='Enter the year of the vehicle', type=int)
@click.option('--price', prompt='Enter the price of the vehicle', type=int)
def add_vehicle(make, model, year, price):
    """Add a new vehicle to the inventory."""
    db = SessionLocal()
    vehicle = Vehicle(make=make, model=model, year=year, price=price)
    db.add(vehicle)
    db.commit()
    db.close()
    click.echo('Vehicle added successfully.')

@cli.command()
@click.option('--vehicle_make', prompt='Enter the MAKE of the vehicle to search/delete')
def search_vehicle(vehicle_make):
    """Search for a vehicle by MAKE."""
    db = SessionLocal()
    vehicle = db.query(Vehicle).filter_by(make=vehicle_make).first()
    db.close()

    if not vehicle:
        click.echo(f'No vehicle found with MAKE {vehicle_make}.')
    else:
        click.echo(f'Vehicle ID: {vehicle.id}, Make: {vehicle.make}, Model: {vehicle.model}, Year: {vehicle.year}, Price: {vehicle.price}')


@cli.command()
def list_vehicles():
    """List all vehicles in the inventory."""
    db = SessionLocal()
    vehicles = db.query(Vehicle).all()
    db.close()

    if not vehicles:
        click.echo('No vehicles found in the inventory.')
    else:
        click.echo('List of vehicles:')
        for vehicle in vehicles:
            click.echo(f'ID: {vehicle.id}, Make: {vehicle.make}, Model: {vehicle.model}, Year: {vehicle.year}, Price: {vehicle.price}')

@cli.command()
@click.option('--vehicle_id', prompt='Enter the ID of the vehicle for the transaction', type=int)
@click.option('--customer_id', prompt='Enter the ID of the customer for the transaction', type=int)
@click.option('--transaction_date', prompt='Enter the transaction date (YYYY-MM-DD)')
def add_transaction(vehicle_id, customer_id, transaction_date):
    """Add a new transaction."""
    try:
        transaction_date = datetime.strptime(transaction_date, '%Y-%m-%d').date()
    except ValueError:
        click.echo('Invalid date format. Please use YYYY-MM-DD format.')
        return

    db = SessionLocal()
    transaction = Transaction(vehicle_id=vehicle_id, customer_id=customer_id, transaction_date=transaction_date)
    db.add(transaction)
    db.commit()
    db.close()
    click.echo('Transaction added successfully.')

@cli.command()
@click.option('--transaction_id', prompt='Enter the ID of the transaction to search/delete', type=int)
def search_transaction(transaction_id):
    """Search for a transaction by ID."""
    db = SessionLocal()
    transaction = db.query(Transaction).filter_by(id=transaction_id).first()
    db.close()

    if not transaction:
        click.echo(f'No transaction found with ID {transaction_id}.')
    else:
        click.echo(f'Transaction ID: {transaction.id}, Vehicle ID: {transaction.vehicle_id}, Customer ID: {transaction.customer_id}, Transaction Date: {transaction.transaction_date}')

@cli.command()
@click.option('--transaction_id', prompt='Enter the ID of the transaction to delete', type=int)
def delete_transaction(transaction_id):
    """Delete a transaction by ID."""
    db = SessionLocal()
    transaction = db.query(Transaction).filter_by(id=transaction_id).first()

    if not transaction:
        db.close()
        click.echo(f'No transaction found with ID {transaction_id}.')
    else:
        db.delete(transaction)
        db.commit()
        db.close()
        click.echo(f'Transaction with ID {transaction_id} deleted successfully.')

@cli.command()
@click.option('--name', prompt='Enter the name of the customer')
@click.option('--email', prompt='Enter the email of the customer')
@click.option('--phone_number', prompt='Enter the phone number of the customer')
def add_customer(name, email, phone_number):
    """Add a new customer."""
    db = SessionLocal()
    customer = Customer(name=name, email=email, phone_number=phone_number)
    db.add(customer)
    db.commit()
    db.close()
    click.echo('Customer added successfully.')

@cli.command()
@click.option('--customer_id', prompt='Enter the ID of the customer to search/delete', type=int)
def search_customer(customer_id):
    """Search for a customer by ID."""
    db = SessionLocal()
    customer = db.query(Customer).filter_by(id=customer_id).first()
    db.close()

    if not customer:
        click.echo(f'No customer found with ID {customer_id}.')
    else:
        click.echo(f'Customer ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone Number: {customer.phone_number}')

@cli.command()
@click.option('--customer_id', prompt='Enter the ID of the customer to delete', type=int)
def delete_customer(customer_id):
    """Delete a customer by ID."""
    db = SessionLocal()
    customer = db.query(Customer).filter_by(id=customer_id).first()

    if not customer:
        db.close()
        click.echo(f'No customer found with ID {customer_id}.')
    else:
        db.delete(customer)
        db.commit()
        db.close()
        click.echo(f'Customer with ID {customer_id} deleted successfully.')

@cli.command()
def list_customers():
    """List all customers in the inventory."""
    db = SessionLocal()
    customers = db.query(Customer).all()
    db.close()

    if not customers:
        click.echo('No customers found in the inventory.')
    else:
        click.echo('List of customers:')
        for customer in customers:
            click.echo(f'ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone Number: {customer.phone_number}')

@cli.command()
def list_transactions():
    """List all transactions in the inventory."""
    db = SessionLocal()
    transactions = db.query(Transaction).all()
    db.close()

    if not transactions:
        click.echo('No transactions found in the inventory.')
    else:
        click.echo('List of transactions:')
        for transaction in transactions:
            click.echo(f'Transaction ID: {transaction.id}, Vehicle ID: {transaction.vehicle_id}, Customer ID: {transaction.customer_id}, Transaction Date: {transaction.transaction_date}, ')

if __name__ == '__main__':
    cli()
