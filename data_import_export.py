import os
import django
import csv

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from webapp.models import Person

# Export data to CSV file
def export_data():
    with open('person_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email', 'Age'])  # CSV header

        for person in Person.objects.all():
            writer.writerow([person.name, person.email, person.age])  # Write each record

    print("Data exported to person_data.csv")

# Import data from CSV file into database
def import_data():
    with open('person_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            Person.objects.create(name=row[0], email=row[1], age=row[2])  # Insert each record into database

    print("Data imported from person_data.csv")

if __name__ == "__main__":
    export_data()
    # Uncomment below line to test importing data.
    # import_data()
