import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from webapp.models import Person

def clean_person_data():
    seen_emails = set()  # Track unique emails to avoid duplicates

    for person in Person.objects.all():
        if person.email in seen_emails:
            person.delete()  # Delete duplicate email entries
        else:
            seen_emails.add(person.email)
            person.name = person.name.title()  # Format names to title case (e.g., "john doe" -> "John Doe")
            person.save()

    print("Person data cleaned and formatted!")

if __name__ == "__main__":
    clean_person_data()
