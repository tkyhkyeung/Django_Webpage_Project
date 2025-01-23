import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from webapp.models import Person, Product, Order  # Import your models
from faker import Faker  # Library for generating fake data
import random

fake = Faker()

# Generate sample data for Person model
for _ in range(20):  # Create 20 records
    Person.objects.create(
        name=fake.name(),  # Generate a random name
        email=fake.email(),  # Generate a random email
        age=random.randint(18, 80)  # Random age between 18 and 80
    )

# Generate sample data for Product model
for _ in range(20):  # Create 20 records
    Product.objects.create(
        name=fake.word().capitalize(),  # Generate a random word as product name
        price=round(random.uniform(10, 500), 2),  # Random price between $10 and $500
        stock=random.randint(1, 100)  # Random stock quantity between 1 and 100
    )

# Generate sample data for Order model
persons = list(Person.objects.all())  # Get all Person records
products = list(Product.objects.all())  # Get all Product records

for _ in range(20):  # Create 20 records
    Order.objects.create(
        person=random.choice(persons),  # Randomly assign a Person to the order
        product=random.choice(products),  # Randomly assign a Product to the order
        quantity=random.randint(1, 5)  # Random quantity between 1 and 5
    )

print("Sample data populated successfully!")
